from typing_extensions import Literal

from pydantic import BaseModel, Field

class CustomerTicket(BaseModel):
    customer_name: str
    customer_message: str

class CustomerInfo(BaseModel):
    sentiment: Literal["positive", "neutral", "frustrated", "angry"]
    urgency: Literal["low", "medium", "high"]


class IssueInfo(BaseModel):
    category: str
    product: str
    description: str
    troubleshooting_attempted: list[str]


class ResolutionRequest(BaseModel):
    requested_action: str


class SupportTicket(BaseModel):
    customer: CustomerInfo
    issue: IssueInfo
    resolution: ResolutionRequest
    order_id: str | None = None
    purchase_date: str | None = None

class RoutingDecision(BaseModel):
    priority: Literal["high", "medium", "low"]
    reason: str
    destination: Literal["human", "queue", "auto_reply"]

class TicketRecord(BaseModel):
    ticket_id: str
    ticket: CustomerTicket
    analysis: SupportTicket | None = None