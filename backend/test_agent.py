from agent import explain_churn, generate_strategy, generate_message

sample_customer = {
    "tenure": 5,
    "MonthlyCharges": 80,
    "Contract": "Month-to-month"
}

prob = 0.82

print("---- WHY ----")
print(explain_churn(sample_customer, prob))

print("\n---- STRATEGY ----")
print(generate_strategy(sample_customer))

print("\n---- MESSAGE ----")
print(generate_message(sample_customer))