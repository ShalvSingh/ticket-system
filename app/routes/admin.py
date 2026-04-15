from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.ticket import Ticket
from app.core.deps import get_current_user
from app.models.user import User

router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("/stats")
def get_stats(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # 🔐 Only admin allowed
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin access only")

    total = db.query(Ticket).count()
    open_tickets = db.query(Ticket).filter(Ticket.status == "open").count()
    closed_tickets = db.query(Ticket).filter(Ticket.status == "closed").count()

    return {
        "total_tickets": total,
        "open_tickets": open_tickets,
        "closed_tickets": closed_tickets
    }