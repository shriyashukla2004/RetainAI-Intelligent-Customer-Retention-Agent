from groq import Groq

# Initialize client
client = Groq(api_key="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")

# -------------------------------
# 1. Explain churn
# -------------------------------
def explain_churn(customer_data, churn_prob):
    prompt = f"""
    You are a customer retention expert.

    Customer Data:
    {customer_data}

    Churn Probability: {churn_prob}

    Explain WHY this customer is likely to churn in simple business terms.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


# -------------------------------
# 2. Retention strategy
# -------------------------------
def generate_strategy(customer_data):
    prompt = f"""
    Suggest a personalized retention strategy for this customer.

    Customer Data:
    {customer_data}

    Be specific and actionable.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


# -------------------------------
# 3. Message generator
# -------------------------------
def generate_message(customer_data):
    prompt = f"""
        Write a short retention message.

        Output format:
        Just the message. Nothing else.

        Customer Data:
    {customer_data}
    At the end write:
    With best Regards
    SHRIYA
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content