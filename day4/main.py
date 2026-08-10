

# from providers.gemini import GeminiProvider
# from providers.groqai import GroqProvider
from schemas import  TicketRecord
from services.router import route_ticket, execute_routing
from services.ticket_generator import generate_ticket
from services.ticket_analyzer import analyze_ticket


# gemini_provider = GeminiProvider()
# groq_provider = GroqProvider()

tickets: list[TicketRecord] = []

# def generate_ticket():
#   prompt = ticket_generation_prompt
#   generated_ticket = groq_provider.generate(prompt)

# # Validate Groq's JSON response with Pydantic
#   ticket = CustomerTicket.model_validate_json(generated_ticket)

#   return ticket


# Generate a list of tickets
for i in range(2):
    ticket = generate_ticket()
    ticket_record = TicketRecord(
        ticket_id=f"TKT-{i + 1:04d}",
        ticket=ticket
    )
    tickets.append(ticket_record)

print(f"Generated {len(tickets)} tickets")

for ticket in tickets:
    print(ticket.model_dump_json(indent=2))

# def analyze_ticket(ticket: CustomerTicket) -> SupportTicket:
#     analysis_prompt = ticket_analysis_prompt.format(
#         ticket_text=ticket.customer_message
#     )

#     response = gemini_provider.generate(analysis_prompt)

#     return SupportTicket.model_validate_json(response)

#Analyze each ticket and print the analysis results
for ticket_record in tickets:
    ticket_record.analysis = analyze_ticket(ticket_record.ticket)
    print(ticket_record.analysis.model_dump_json(indent=2))


# def route_ticket(routing_analysis: SupportTicket) -> RoutingDecision:
#     routing_prompt = routing_decision_prompt.format(analysis=routing_analysis.customer.model_dump_json(indent=2))

#     response = groq_provider.generate(routing_prompt)

#     return RoutingDecision.model_validate_json(response)

#Execute routing for each ticket based on the analysis and print the routing decision
for ticket_record in tickets:
    ticket_record.routing = route_ticket(ticket_record.analysis)
    print(ticket_record.routing.model_dump_json(indent=2))
    execute_routing(ticket_record)