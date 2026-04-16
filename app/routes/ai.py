from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.ticket import Ticket
from app.core.deps import get_current_user
from app.models.user import User

router = APIRouter(prefix="/ai", tags=["AI"])


@router.get("/query")
def ai_query(
    q: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = db.query(Ticket)

    # User restriction
    if current_user.role != "admin":
        query = query.filter(Ticket.created_by == current_user.username)

    q_lower = q.lower()

    # Simple NLP logic
    if "high" in q_lower:
        query = query.filter(Ticket.priority == "high")

    if "open" in q_lower:
        query = query.filter(Ticket.status == "open")

    if "closed" in q_lower:
        query = query.filter(Ticket.status == "closed")

    return {
        "query": q,
        "results": query.all()
    }