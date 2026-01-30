import pandas as pd
import numpy as np

print("===== SUPERSTORE DATA CLEANING PIPELINE STARTED =====")

# ==============================
# STEP 1: LOAD DATA
# ==============================
df = pd.read_csv("data/Sample - Superstore.csv", encoding="latin1")
print("Initial Shape:", df.shape)

# ==============================
# STEP 2: DATA DICTIONARY (SAFE)
# ==============================
data_dictionary = pd.DataFrame({
    "Column Name": df.columns,
    "Data Type": df.dtypes.astype(str),
    "Non-Null Count": df.notnull().sum(),
    "Business Description": ["To be documented"] * len(df.columns)
})

data_dictionary.to_csv("data_dictionary.csv", index=False)
print("Data dictionary created")

# ==============================
# STEP 3: DATA PROFILING
# ==============================
print("\nMissing Values:\n", df.isnull().sum())
print("Duplicate Rows:", df.duplicated().sum())

# ==============================
# STEP 4: DATA CLEANING
# ==============================

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert date columns
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

# Handle missing postal codes
if "Postal Code" in df.columns:
    df["Postal Code"].fillna(0, inplace=True)

# Standardize text columns
text_columns = [
    "Ship Mode", "Segment", "Country", "City",
    "State", "Region", "Category", "Sub-Category"
]

for col in text_columns:
    if col in df.columns:
        df[col] = df[col].astype(str).str.lower().str.strip()

# ==============================
# STEP 5: FEATURE ENGINEERING
# ==============================

# Shipping duration
df["Shipping_Days"] = (df["Ship Date"] - df["Order Date"]).dt.days

# Profit margin (avoid division by zero)
df["Profit_Margin"] = np.where(
    df["Sales"] != 0,
    df["Profit"] / df["Sales"],
    0
)

# Order year and month
df["Order_Year"] = df["Order Date"].dt.year
df["Order_Month"] = df["Order Date"].dt.month

# Discount flag
df["High_Discount"] = np.where(df["Discount"] > 0.2, "yes", "no")

# ==============================
# STEP 6: FINAL VALIDATION
# ==============================
print("\nFinal Shape:", df.shape)
print("\nFinal Missing Values:\n", df.isnull().sum())

# ==============================
# STEP 7: EXPORT CLEAN DATA
# ==============================
df.to_csv("cleaned_superstore_data.csv", index=False)

print("\n✅ CLEANED DATASET SAVED AS: cleaned_superstore_data.csv")
print("===== DATA CLEANING PIPELINE COMPLETED SUCCESSFULLY =====")
