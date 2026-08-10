from typing_extensions import Literal

from pydantic import BaseModel, Field

## Pydantic models for customer support ticketing system
class CustomerTicket(BaseModel):
    customer_name: str
    customer_message: str

# Pydantic models for Customer sentiment and urgency
class CustomerInfo(BaseModel):
    sentiment: Literal["positive", "neutral", "frustrated", "angry"]
    urgency: Literal["low", "medium", "high"]

# Pydantic models for ticket analysis
class IssueInfo(BaseModel):
    category: str
    product: str
    description: str
    troubleshooting_attempted: list[str]

# Pydantic models for ticket analysis and routing
class ResolutionRequest(BaseModel):
    requested_action: str

# Pydantic model for support ticket analysis - Validates the analysis of a customer support ticket and extracts relevant information.
class SupportTicket(BaseModel):
    customer: CustomerInfo
    issue: IssueInfo
    resolution: ResolutionRequest
    order_id: str | None = None
    purchase_date: str | None = None

# Pydantic model for routing decisions
class RoutingDecision(BaseModel):
    priority: Literal["high", "medium", "low"]
    reason: str
    destination: Literal["human", "queue", "auto_reply"]

class AutoReply(BaseModel):
    response: str

# Pydantic model for ticket records - Represents a complete lifecyclerecord of a customer support ticket, including its ID, the original ticket, the analysis, and the routing decision.
class TicketRecord(BaseModel):
    ticket_id: str
    ticket: CustomerTicket
    analysis: SupportTicket | None = None
    routing: RoutingDecision | None = None
    auto_reply: AutoReply | None = None