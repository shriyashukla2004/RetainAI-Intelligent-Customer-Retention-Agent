from fastapi import FastAPI
import joblib
import pandas as pd

from backend.agent import explain_churn, generate_strategy, generate_message

app = FastAPI()

# -------------------------------
# Load ML model
# -------------------------------
model = joblib.load("ml/churn_model.pkl")
columns = joblib.load("ml/columns.pkl")

# -------------------------------
# Helper function
# -------------------------------
def predict_churn(input_data: dict):
    df = pd.DataFrame([input_data])
    df = df.reindex(columns=columns, fill_value=0)
    
    prob = model.predict_proba(df)[0][1]
    return prob

# -------------------------------
# Main API
# -------------------------------
@app.post("/analyze_customer")
def analyze_customer(data: dict):
    
    # 1. Predict churn
    churn_prob = predict_churn(data)

    # 2. AI explanation
    explanation = explain_churn(data, churn_prob)

    # 3. Strategy
    strategy = generate_strategy(data)

    # 4. Message
    message = generate_message(data)

    return {
        "churn_probability": float(churn_prob),
        "explanation": explanation,
        "strategy": strategy,
        "message": message
    }