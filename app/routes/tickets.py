from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.ticket import Ticket
# from app.schemas.ticket import TicketCreate
from app.core.deps import get_current_user
from app.models.user import User
from typing import Optional
from fastapi import HTTPException
from app.schemas.ticket import TicketCreate, TicketUpdate 


router = APIRouter(prefix="/tickets", tags=["Tickets"])


@router.post("/")
def create_ticket(
    ticket: TicketCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_ticket = Ticket(
        title=ticket.title,
        description=ticket.description,
        priority=ticket.priority,
        category=ticket.category,
        created_by=current_user.username
    )

    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)

    return new_ticket


@router.get("/")
def get_tickets(
    status: Optional[str] = None,
    priority: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = db.query(Ticket)

    # User vs Admin
    if current_user.role != "admin":
        query = query.filter(Ticket.created_by == current_user.username)

    # Filters
    if status:
        query = query.filter(Ticket.status == status)

    if priority:
        query = query.filter(Ticket.priority == priority)

    return query.all()


@router.get("/{ticket_id}")
def get_ticket_by_id(
    ticket_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    # 🔐 User can only access their own ticket
    if current_user.role != "admin" and ticket.created_by != current_user.username:
        raise HTTPException(status_code=403, detail="Not authorized")

    return ticket 


@router.put("/{ticket_id}")
def update_ticket(
    ticket_id: int,
    ticket_data: TicketUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    # 🔐 Only owner or admin
    if current_user.role != "admin" and ticket.created_by != current_user.username:
        raise HTTPException(status_code=403, detail="Not authorized")

    # 🔄 Update fields
    if ticket_data.title:
        ticket.title = ticket_data.title
    if ticket_data.description:
        ticket.description = ticket_data.description
    if ticket_data.priority:
        ticket.priority = ticket_data.priority
    if ticket_data.category:
        ticket.category = ticket_data.category

    db.commit()
    db.refresh(ticket)

    return ticket



@router.patch("/{ticket_id}/status")
def update_ticket_status(
    ticket_id: int,
    status: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    # 🔐 Only owner or admin
    if current_user.role != "admin" and ticket.created_by != current_user.username:
        raise HTTPException(status_code=403, detail="Not authorized")

    ticket.status = status

    db.commit()
    db.refresh(ticket)

    return ticket



@router.delete("/{ticket_id}")
def delete_ticket(
    ticket_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    # 🔐 Only owner or admin
    if current_user.role != "admin" and ticket.created_by != current_user.username:
        raise HTTPException(status_code=403, detail="Not authorized")

    db.delete(ticket)
    db.commit()

    return {"message": "Ticket deleted successfully"}



