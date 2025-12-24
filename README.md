# 📉 Customer Churn Prediction

## 🚀 Project Overview
Customer churn refers to customers stopping the use of a company’s service.  
Predicting churn helps businesses retain customers by taking proactive actions.

This project builds an **end-to-end Machine Learning solution** that predicts whether a customer is likely to churn based on their usage, billing, and service information. It also provides a **Flask web application** for real-time churn prediction.

---

## 🎯 Business Problem
Customer acquisition is expensive. Losing customers early leads to revenue loss.

**Goal:**
- Predict customer churn probability
- Classify customers into **High / Low risk**
- Help businesses focus on retention strategies

---

## 📊 Dataset
- **Dataset:** Telco Customer Churn
- **Records:** 7,043
- **Target Variable:** `Churn`
  - `1` → Customer churned
  - `0` → Customer retained

### Important Features
| Feature | Description |
|------|------------|
| tenure | Number of months customer stayed |
| MonthlyCharges | Monthly subscription fee |
| TotalCharges | Total amount paid |
| Contract | Contract type |
| InternetService | Internet service type |
| PaymentMethod | Payment method |

---

## 🧪 Project Workflow

### 1️⃣ Exploratory Data Analysis (EDA)
- Handled missing values in `TotalCharges`
- Removed duplicates
- Visualized churn distribution
- Analyzed churn vs tenure, monthly charges, and contract type

### 2️⃣ Feature Engineering
- Created `tenure_group`
- Converted service inconsistencies
- Engineered new features:
  - `total_addons`
  - `high_value_customer`

### 3️⃣ Preprocessing
- Numerical scaling using **StandardScaler**
- Categorical encoding using **OneHotEncoder**
- Used **ColumnTransformer** for clean preprocessing

---

## 🤖 Model Building
- Logistic Regression (baseline)
- **Random Forest Classifier (final model)**

### Model Highlights
- Handles class imbalance
- Captures non-linear patterns
- Pipeline ensures consistency during inference

### Evaluation Metrics
- Precision, Recall, F1-Score
- ROC-AUC Score

---

## 🌐 Web Application (Flask)

### Features
- User inputs:
  - Tenure
  - Monthly Charges
  - Total Charges
- Outputs:
  - Churn Probability
  - Risk Level (High / Low)
- Probability visualization bar

---

## 🖥️ Project Structure

