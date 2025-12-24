from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("churn_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

def get_tenure_group(tenure):
    if tenure <= 12:
        return "0-12"
    elif tenure <= 24:
        return "12-24"
    elif tenure <= 48:
        return "24-48"
    elif tenure <= 60:
        return "48-60"
    else:
        return "60+"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    tenure = int(data["tenure"])
    monthly = float(data["MonthlyCharges"])
    total = float(data["TotalCharges"])

    input_data = {
        "customerID": "TEMP-USER",
        "gender": "Male",
        "SeniorCitizen": 0,
        "Partner": "No",
        "Dependents": "No",
        "tenure": tenure,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "DSL",
        "OnlineSecurity": "No",
        "OnlineBackup": "No",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "No",
        "StreamingMovies": "No",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": monthly,
        "TotalCharges": total,
        "tenure_group": get_tenure_group(tenure),
        "total_addons": 0,
        "high_value_customer": int(monthly > 70)
    }

    df = pd.DataFrame([input_data])

    prob = model.predict_proba(df)[0][1]

    return jsonify({
        "churn_probability": round(float(prob), 3),
        "risk": "High" if prob >= 0.5 else "Low"
    })

if __name__ == "__main__":
    app.run(debug=True)
