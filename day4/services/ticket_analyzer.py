from providers.gemini import GeminiProvider
from schemas import CustomerTicket, SupportTicket
from prompts import ticket_analysis_prompt

gemini_provider = GeminiProvider()


def analyze_ticket(ticket: CustomerTicket) -> SupportTicket:

    analysis_prompt = ticket_analysis_prompt.format(
        ticket_text=ticket.customer_message,
        schema=SupportTicket.model_json_schema()
    )

    response = gemini_provider.generate(
        analysis_prompt
    )

    return SupportTicket.model_validate_json(
        response
    )