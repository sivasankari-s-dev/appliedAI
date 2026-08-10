
# ticket_generation_prompt = """Generate a realistic customer-service ticket. Vary the customer's tone, problem, product, severity, and amount of detail. Some customers should be calm, some frustrated, and some angry. Include enough information for another AI system to determine priority, but do not explicitly state the priority or severity"""
ticket_generation_prompt = """
Generate a realistic random customer service ticket.No Duplicates allowed.

Return ONLY valid JSON with these fields:

{
    "customer_name": "customer name",
    "customer_message": "natural customer service message"
}

The ticket must describe ONE realistic customer problem.

IMPORTANT:
- Do not include ticket_id. The application will generate it.
- Do not explicitly state sentiment.
- Do not explicitly state urgency.
- Do not explicitly state severity.
- Do not explicitly state priority.
- Do not explicitly state the issue category.
- Put all relevant information naturally inside customer_message.

Vary the tickets significantly. Across multiple generations, use different
products, problems, customer situations, and writing styles.

Possible problem types include, but are not limited to:
- damaged product
- defective product
- missing delivery
- delayed delivery
- wrong product received
- incomplete order
- duplicate payment
- unexpected charge
- refund request
- account/login problem
- subscription problem
- cancellation request
- product information question
- warranty issue
- replacement request
- billing problem

Do not repeatedly use the same problem type or sentence structure.

Some customers should provide detailed information.
Some should provide very little information.
Some should be calm.
Some should be frustrated.
Some should be angry.
Some should simply ask a question.

Do not tell the downstream system what the priority or sentiment should be.

Return only valid JSON.
"""

ticket_analysis_prompt = """You are a customer service ticket analysis system.

Analyze the customer service ticket provided below and extract the relevant information.

Follow these rules:

1. Analyze the customer's message carefully and identify their emotional sentiment.
2. Classify sentiment as one of: positive, neutral, frustrated, or angry.
3. Assess the urgency of the issue as low, medium, or high based on the customer's situation and language.
4. Identify the main issue category.
5. Identify the product or service involved.
6. Provide a concise but accurate description of the customer's problem.
7. List all troubleshooting steps the customer explicitly mentions attempting. If none are mentioned, return an empty list.
8. Identify the action or resolution the customer is requesting.
9. Extract the order ID if one is present. If it is not present, return null.
10. Extract the purchase date if one is present. If it is not present, return null.If the customer gives a relative time such as "two weeks ago", "last month", or "yesterday", preserve the statement exactly rather than converting it into an exact calendar date. Never infer an exact date unless one is explicitly provided in the ticket.
11. Do not invent information that is not present in the ticket.
12. Use reasonable inference only when necessary to classify sentiment or urgency.
13. Return the result using the provided SupportTicket response schema.
14. Do not include explanations, commentary, markdown, or any fields outside the response schema.

Customer service ticket:

{ticket_text}"""
