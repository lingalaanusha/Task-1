# 📊 Superstore Data Cleaning & Preparation Pipeline

## 📌 Project Overview

This project focuses on the **first and most critical step of data analysis**:
**data acquisition, profiling, cleaning, transformation, and preparation**.

Using the **Sample Superstore sales transactions dataset**, the project delivers an **analysis-ready dataset** along with a **data dictionary** and a fully automated **Python cleaning pipeline**.

---

## 🎯 Objectives

* Understand and explore a real-world business dataset
* Identify and handle data quality issues
* Perform feature engineering for business insights
* Produce a clean dataset ready for analysis or modeling

---

## 📂 Dataset Used

**Name:** Sample – Superstore
**Type:** Sales Transactions & Customer Data

### Key Attributes:

* Order & Shipping dates
* Customer and regional information
* Product categories
* Sales, profit, discount, quantity

---

## 🛠 Tools & Technologies

* **Python 3**
* **Pandas**
* **NumPy**

---

## 🔄 Process Workflow

### 1️⃣ Data Loading

* Loaded CSV dataset using Pandas
* Verified structure, shape, and schema

### 2️⃣ Data Dictionary Creation

* Automatically generated a data dictionary containing:

  * Column names
  * Data types
  * Non-null counts
  * Business description placeholder

📄 Output: `data_dictionary.csv`

---

### 3️⃣ Data Profiling

Identified common data issues such as:

* Missing values (e.g., Postal Code)
* Duplicate records
* Inconsistent text formatting

---

### 4️⃣ Data Cleaning

* Removed duplicate records
* Converted date columns to datetime format
* Handled missing postal codes
* Standardized categorical text fields

---

### 5️⃣ Feature Engineering

Created new, meaningful features:

* **Shipping_Days** → Delivery duration
* **Profit_Margin** → Profitability indicator
* **Order_Year & Order_Month** → Time-based analysis
* **High_Discount** → Flag for high discounts

---

### 6️⃣ Final Validation

* Rechecked missing values
* Verified dataset shape after transformations

---

### 7️⃣ Export Clean Dataset

📄 Output: `cleaned_superstore_data.csv`
Ready for analysis, visualization, or machine learning.

---

## 📁 Project Structure

```
data_analytics_internship/
│
├── data/
│   └── Sample - Superstore.csv
│
├── data_cleaning.py
├── data_dictionary.csv
├── cleaned_superstore_data.csv
└── README.md
```

---

## ▶️ How to Run the Project

```bash
python data_cleaning.py
```

---

## 📦 Deliverables

* ✅ Data dictionary
* ✅ Cleaned, analysis-ready dataset
* ✅ Python data cleaning pipeline
* ✅ Documentation (README)

---

## 🏆 Key Learnings

* Importance of data quality before analysis
* Handling real-world messy data
* Writing robust and reusable cleaning scripts
* Feature engineering for business insights

---

## Output

https://github.com/user-attachments/assets/d3c2d254-1de4-4c96-b49d-7943d8afcc1e
