from providers.gemini import GeminiProvider
from schemas import AutoReply,  TicketRecord
from prompts import auto_reply_prompt

# Gemini is the provider used for generating automatic replies to customer tickets.
gemini_provider = GeminiProvider()

# Generate an automatic reply to the customer based on the ticket analysis.
# def generate_auto_reply(ticket_record: TicketRecord) -> str:

#     prompt = auto_reply_prompt.format(
#         ticket=ticket_record.ticket.model_dump_json(indent=2),
#         analysis=ticket_record.analysis.model_dump_json(indent=2)
#     )
def generate_auto_reply(
    ticket_record: TicketRecord
) -> AutoReply:

    prompt = auto_reply_prompt.format(
        ticket=ticket_record.ticket.model_dump_json(indent=2),
        analysis=ticket_record.analysis.model_dump_json(indent=2)
    )
    auto_reply_response = gemini_provider.generate(prompt)
    print(auto_reply_response)
    # return auto_reply_response
    return AutoReply.model_validate_json(auto_reply_response)