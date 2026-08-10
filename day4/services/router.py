from urllib import response

from schemas import SupportTicket, RoutingDecision, TicketRecord
from providers.groqai import GroqProvider
from prompts import routing_decision_prompt
from services.responder import generate_auto_reply

#Groq is the provider used for routing decisions.
groq_provider = GroqProvider()

#Groq routing decision function that takes a SupportTicket and returns a RoutingDecision.
def route_ticket(routing_analysis: SupportTicket) -> RoutingDecision:

    routing_prompt = routing_decision_prompt.format(analysis=routing_analysis.model_dump_json(indent=2))

    routing_decision_response = groq_provider.generate(routing_prompt)

    print(f"Routing response: {routing_decision_response}")
    return RoutingDecision.model_validate_json(routing_decision_response)

#Sending the ticket to a human support agent for immediate attention.
def escalate_to_human(ticket_record: TicketRecord):
    print(f"🚨 {ticket_record.ticket_id} → HUMAN ESCALATION")

#Sending the ticket to the support queue for normal processing.
def add_to_queue(ticket_record: TicketRecord):
    print(f"📥 {ticket_record.ticket_id} → SUPPORT QUEUE")

#sending an automatic reply to the customer based on the ticket analysis.
def trigger_auto_reply(ticket_record: TicketRecord):
      response = generate_auto_reply(ticket_record)
      print(f"\n🤖 {ticket_record.ticket_id} → AUTO REPLY")
      print(response)

#Based on the Groq routing decision, execute the appropriate action for the ticket.
def execute_routing(ticket_record: TicketRecord):

    if ticket_record.routing.destination == "human":
        escalate_to_human(ticket_record)

    elif ticket_record.routing.destination == "queue":
        add_to_queue(ticket_record)

    elif ticket_record.routing.destination == "auto_reply":
        trigger_auto_reply(ticket_record)

    else:
        raise ValueError(
            f"Unknown destination: "
            f"{ticket_record.routing.destination}"
        )