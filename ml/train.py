import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier

# -------------------------------
# 1. Load Data
# -------------------------------
df = pd.read_csv(r"C:\Users\KIIT\Desktop\AI Customer Retention Agent\ai-retention-agent\data\telco.csv")

print(df.head())

# -------------------------------
# 2. Data Cleaning
# -------------------------------

# Fix TotalCharges (important)
df["TotalCharges"] = pd.to_numeric(df["Total Charges"], errors="coerce")

# Use correct target column
df["Churn"] = df["Churn Value"]

# Drop unnecessary columns
df = df.drop(["customerID", "Churn Value", "Churn Label"], axis=1, errors="ignore")

# Fill missing values instead of dropping
df = df.fillna(0)

# -------------------------------
# 3. Encode Categorical Variables
# -------------------------------
df = pd.get_dummies(df, drop_first=True)
print("Churn distribution:\n", df["Churn"].value_counts())
# -------------------------------
# 4. Split Data
# -------------------------------
X = df.drop("Churn", axis=1)
y = df["Churn"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# 5. Train Model
# -------------------------------
model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
model.fit(X_train, y_train)

# -------------------------------
# 6. Evaluate
# -------------------------------
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

# -------------------------------
# 7. Save Model + Columns
# -------------------------------
joblib.dump(model, "ml/churn_model.pkl")
joblib.dump(X.columns.tolist(), "ml/columns.pkl")

print("Model saved successfully ✅")
