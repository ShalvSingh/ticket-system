from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin
from app.core.security import hash_password, verify_password
from app.core.auth import create_access_token
from app.core.deps import get_current_user
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(prefix="/auth", tags=["auth"])


# Authentication routes -> it is register api
@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    
    existing_user = db.query(User).filter(
        (User.username == user.username) | (User.email == user.email)
    ).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    try:
        new_user = User(
            username=user.username,
            email=user.email,
            password=hash_password(user.password),
            role="admin"

        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return {"message": "User registered successfully"}

    except Exception as e:
        print("ERROR:", e)   # 🔥 THIS WILL SHOW REAL ERROR
        raise HTTPException(status_code=500, detail="Something went wrong")


        

# authentication -> it is login api

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == form_data.username).first()

    if not db_user or not verify_password(form_data.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({
        "sub": db_user.username,
        "role": db_user.role
    })

    return {"access_token": token, "token_type": "bearer"}

# protected route 

@router.get("/me")
def get_me(current_user: User = Depends(get_current_user)):
    return {
        "username": current_user.username,
        "email": current_user.email,
        "role": current_user.role
    }