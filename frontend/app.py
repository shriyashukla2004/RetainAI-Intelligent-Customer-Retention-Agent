import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="AI Retention Agent", layout="centered")

# -------------------------------
# CUSTOM CSS
# -------------------------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
h1 {
    color: #4CAF50;
    text-align: center;
}
.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: bold;
}
[data-testid="stMetricValue"] {
    color: #4CAF50;
}
section[data-testid="stSidebar"] {
    background-color: #111827;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# LOAD DATASET (REAL DATA)
# -------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\KIIT\Desktop\AI Customer Retention Agent\ai-retention-agent\data\telco.csv")
    df["Churn"] = df["Churn Value"]
    return df

df = load_data()

# -------------------------------
# SIDEBAR
# -------------------------------
st.sidebar.title("📊 Dashboard")

view = st.sidebar.radio("Select View", [
    "Customer Analysis",
    "Dashboard Overview"
])

# -------------------------------
# HEADER
# -------------------------------
col1, col2 = st.columns([1, 4])

with col1:
    st.image("frontend/logo.jpg", width=80)

with col2:
    st.title("RetainAI: Intelligent Customer Retention Agent")

st.markdown("### Smart AI system for predicting and preventing customer churn")

# =====================================================
# 🟢 CUSTOMER ANALYSIS (AI AGENT)
# =====================================================
if view == "Customer Analysis":

    st.subheader("🔍 Analyze Individual Customer")

    tenure = st.number_input("Tenure (months)", min_value=0, value=5)
    monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=80.0)
    total_charges = st.number_input("Total Charges", min_value=0.0, value=300.0)

    contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])

    contract_month = 1 if contract == "Month-to-month" else 0
    contract_one = 1 if contract == "One year" else 0
    contract_two = 1 if contract == "Two year" else 0

    if st.button("🚀 Run AI Retention Agent"):

        input_data = {
            "tenure": tenure,
            "Monthly Charges": monthly_charges,
            "Total Charges": total_charges,
            "Contract_Month-to-month": contract_month,
            "Contract_One year": contract_one,
            "Contract_Two year": contract_two
        }

        try:
            response = requests.post(
                "http://127.0.0.1:8000/analyze_customer",
                json=input_data
            )

            result = response.json()

            st.subheader("📊 Churn Probability")
            st.metric("Risk Score", f"{result['churn_probability']:.2f}")

            st.subheader("🧠 Why is this customer churning?")
            st.write(result["explanation"])

            st.subheader("🎯 Recommended Strategy")
            st.write(result["strategy"])

            st.subheader("💬 Final Message")
            st.success(result["message"])

        except Exception as e:
            st.error(f"Error: {e}")

# =====================================================
# 🔵 DASHBOARD OVERVIEW (REAL DATA)
# =====================================================
elif view == "Dashboard Overview":

    st.title("📊 Retention Dashboard")

    # -------------------------------
    # METRICS (REAL DATA)
    # -------------------------------
    total_customers = len(df)
    churned = df[df["Churn"] == 1].shape[0]
    churn_rate = (churned / total_customers) * 100

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Customers", total_customers)
    col2.metric("Churned Customers", churned)
    col3.metric("Churn Rate", f"{churn_rate:.2f}%")

    st.markdown("---")

    # -------------------------------
    # PIE CHART (CHURN DISTRIBUTION)
    # -------------------------------
    churn_dist = df["Churn"].value_counts().reset_index()
    churn_dist.columns = ["Churn", "Count"]

    churn_dist["Churn"] = churn_dist["Churn"].map({
        0: "Active",
        1: "Churned"
    })

    fig1 = px.pie(
        churn_dist,
        names="Churn",
        values="Count",
        title="Customer Churn Distribution"
    )

    st.plotly_chart(fig1, use_container_width=True)

    # -------------------------------
    # BAR CHART (CONTRACT VS CHURN)
    # -------------------------------
    contract_churn = pd.crosstab(df["Contract"], df["Churn"]).reset_index()

    fig2 = px.bar(
        contract_churn,
        x="Contract",
        y=[0, 1],
        title="Churn by Contract Type",
        labels={"value": "Count", "variable": "Churn"},
        barmode="group"
    )

    st.plotly_chart(fig2, use_container_width=True)

    # -------------------------------
    # BOX PLOT (CHURN DRIVERS)
    # -------------------------------
    fig3 = px.box(
        df,
        x="Churn",
        y="Monthly Charges",
        title="Monthly Charges vs Churn"
    )

    st.plotly_chart(fig3, use_container_width=True)