# RetainAI: Intelligent Customer Retention Agent

>  **An end-to-end AI system that predicts customer churn, explains why it happens, and generates personalized retention strategies using Machine Learning and Generative AI.**

---

## Overview

Customer churn is one of the biggest business challenges. Most solutions stop at prediction.

**RetainAI goes beyond prediction.**

### This system:
-  Identifies customers at risk of churn  
-  Explains the reason behind churn (GenAI)  
-  Recommends actionable retention strategies  
-  Generates personalized customer messages  
-  Provides a real-time analytics dashboard  

---

## Key Features

| Feature | Description |
|--------|------------|
|  Churn Prediction | XGBoost-based model |
|  AI Explanation | LLM-powered reasoning |
|  Strategy Generator | Personalized retention actions |
|  Messaging | Automated customer communication |
|  Dashboard | Streamlit + Plotly analytics |
|  API | FastAPI backend |

---

## System Architecture
Streamlit UI
↓
FastAPI Backend
↓
ML Model (XGBoost)
↓
LLM (Groq - LLaMA 3)
↓
Insights + Strategy + Message


---

## Tech Stack

### Languages & Data
- Python, SQL  
- Pandas, NumPy  

### Machine Learning
- Scikit-learn, XGBoost  
- Time Series & Model Evaluation  

### Generative AI
- Groq API (LLaMA 3)  
- Prompt Engineering  
- AI Agents  

### Backend
- FastAPI (REST APIs)  

### Frontend
- Streamlit  

### Visualization
- Plotly  

### Tools
- Git, GitHub, Jupyter Notebook, VS Code  

---

## Dashboard Insights

-  Customer churn distribution  
-  Contract vs churn analysis  
-  Feature-level insights (e.g., Monthly Charges impact)  
-  Real-time AI-generated recommendations  

---

## How It Works

1. User inputs customer data  
2. ML model predicts churn probability  
3. LLM explains the reason behind churn  
4. AI generates retention strategy  
5. System creates a personalized message  

---

## How to Run Locally

1️. Clone the repo
```bash
git clone https://github.com/shriyashukla2004/RetainAI-Intelligent-Customer-Retention-Agent.git
cd retainai

2️. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3️. Install dependencies
pip install -r requirements.txt

4️. Run Backend (FastAPI)
uvicorn backend.main:app --reload

5️. Run Frontend (Streamlit)
streamlit run frontend/app.py

## API Endpoint

POST /analyze_customer
 Example Input
{
  "tenure": 5,
  "MonthlyCharges": 80,
  "TotalCharges": 300,
  "Contract_Month-to-month": 1
}
 Output
{
  "churn_probability": 0.82,
  "explanation": "...",
  "strategy": "...",
  "message": "..."
}

---

## Author

Shriya Shukla
Location: Lucknow, India
Mail: shriyaa0902@gmail.com
LinkedIn: https://www.linkedin.com/in/shriyashukla09/
