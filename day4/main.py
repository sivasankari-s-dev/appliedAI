

from providers.gemini import GeminiProvider
from providers.groqai import GroqProvider
from schemas import CustomerTicket, TicketRecord, SupportTicket
from prompts import ticket_generation_prompt, ticket_analysis_prompt


gemini_provider = GeminiProvider()
groq_provider = GroqProvider()

def generate_ticket():
  prompt = ticket_generation_prompt
  generated_ticket = groq_provider.generate(prompt)

# Validate Groq's JSON response with Pydantic
  ticket = CustomerTicket.model_validate_json(generated_ticket)

  return ticket

tickets: list[TicketRecord] = []

for i in range(10):
    ticket = generate_ticket()
    ticket_record = TicketRecord(
        ticket_id=f"TKT-{i + 1:04d}",
        ticket=ticket
    )
    tickets.append(ticket_record)

print(f"Generated {len(tickets)} tickets")

for ticket in tickets:
    print(ticket.model_dump_json(indent=2))

def analyze_ticket(ticket: CustomerTicket) -> SupportTicket:
    analysis_prompt = ticket_analysis_prompt.format(
        ticket_text=ticket.customer_message
    )

    response = gemini_provider.generate(analysis_prompt)

    return SupportTicket.model_validate_json(response)

for ticket_record in tickets:
    ticket_record.analysis = analyze_ticket(ticket_record.ticket)
    print(ticket_record.analysis.model_dump_json(indent=2))

# analysis_prompt = ticket_analysis_prompt.format(ticket_text=generated_ticket)

# response_text = gemini_provider.generate(analysis_prompt)
# print(response_text)