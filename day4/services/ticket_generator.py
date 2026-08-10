from providers.groqai import GroqProvider
from schemas import CustomerTicket
from prompts import ticket_generation_prompt

groq_provider = GroqProvider()


def generate_ticket() -> CustomerTicket:

    generated_ticket = groq_provider.generate(
        ticket_generation_prompt
    )

    return CustomerTicket.model_validate_json(
        generated_ticket
    )