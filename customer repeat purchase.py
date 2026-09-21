# ============================================================
# CUSTOMER REPEAT PURCHASE ANALYSIS
# ============================================================
import pandas as pd
import matplotlib.pyplot as plt

file_path = "Customer_Repeat_Purchase_Analysis_Dataset.xlsx"

df = pd.read_excel(file_path)

print("Dataset loaded successfully!")
print("\nFirst 5 rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())
# ============================================================
# STEP 1 - CUSTOMER-WISE ORDER COUNT
# ============================================================

customer_orders = (
    df.groupby("CustomerID")["InvoiceNo"]
    .nunique()
    .reset_index()
)

customer_orders.columns = ["CustomerID", "Total_Orders"]

print("\n========== CUSTOMER ORDER COUNT ==========")
print(customer_orders.head(10))


# ============================================================
# STEP 2 - CUSTOMER TYPE
# ============================================================

customer_orders["Customer_Type"] = customer_orders[
    "Total_Orders"
].apply(
    lambda x: "Repeat Customer"
    if x >= 2
    else "First-time Customer"
)

print("\n========== CUSTOMER TYPE ==========")
print(customer_orders.head(10))


# ============================================================
# STEP 3 - TOTAL CUSTOMERS
# ============================================================

total_customers = len(customer_orders)

first_time_customers = (
    customer_orders["Customer_Type"]
    == "First-time Customer"
).sum()

repeat_customers = (
    customer_orders["Customer_Type"]
    == "Repeat Customer"
).sum()

print("\n========== CUSTOMER SUMMARY ==========")
print("Total Customers:", total_customers)
print("First-time Customers:", first_time_customers)
print("Repeat Customers:", repeat_customers)


# ============================================================
# STEP 4 - REPEAT PURCHASE RATE
# ============================================================

repeat_purchase_rate = (
    repeat_customers / total_customers
) * 100

print(
    "\nRepeat Purchase Rate:",
    round(repeat_purchase_rate, 2),
    "%"
)


# ============================================================
# STEP 5 - CUSTOMER REVENUE
# ============================================================

customer_revenue = (
    df.groupby("CustomerID")["Revenue"]
    .sum()
    .reset_index()
)

customer_revenue.columns = [
    "CustomerID",
    "Total_Revenue"
]

print("\n========== CUSTOMER REVENUE ==========")
print(customer_revenue.head(10))


# ============================================================
# STEP 6 - MERGE ORDER + REVENUE DATA
# ============================================================

customer_analysis = pd.merge(
    customer_orders,
    customer_revenue,
    on="CustomerID"
)

print("\n========== CUSTOMER ANALYSIS ==========")
print(customer_analysis.head(10))


# ============================================================
# STEP 7 - AVERAGE ORDER VALUE
# ============================================================

customer_analysis["AOV"] = (
    customer_analysis["Total_Revenue"]
    / customer_analysis["Total_Orders"]
)

print("\n========== AOV ==========")
print(customer_analysis.head(10))


# ============================================================
# STEP 8 - FIRST-TIME VS REPEAT AOV
# ============================================================

first_time_aov = customer_analysis[
    customer_analysis["Customer_Type"]
    == "First-time Customer"
]["AOV"].mean()

repeat_aov = customer_analysis[
    customer_analysis["Customer_Type"]
    == "Repeat Customer"
]["AOV"].mean()

print("\n========== AOV COMPARISON ==========")

print(
    "First-time Customer AOV:",
    round(first_time_aov, 2)
)

print(
    "Repeat Customer AOV:",
    round(repeat_aov, 2)
)


# ============================================================
# STEP 9 - CUSTOMER SEGMENTATION
# ============================================================

def customer_segment(orders):

    if orders == 1:
        return "One-time"

    elif orders <= 3:
        return "Occasional"

    elif orders <= 6:
        return "Regular"

    else:
        return "Loyal"


customer_analysis["Segment"] = (
    customer_analysis["Total_Orders"]
    .apply(customer_segment)
)

print("\n========== CUSTOMER SEGMENTS ==========")
print(
    customer_analysis["Segment"]
    .value_counts()
)


# ============================================================
# STEP 10 - SEGMENT SUMMARY
# ============================================================

segment_summary = (
    customer_analysis
    .groupby("Segment")
    .agg(
        Customers=("CustomerID", "count"),
        Revenue=("Total_Revenue", "sum"),
        Average_AOV=("AOV", "mean")
    )
    .reset_index()
)

print("\n========== SEGMENT SUMMARY ==========")
print(segment_summary)


# ============================================================
# STEP 11 - TOP 10 REPEAT CUSTOMERS
# ============================================================

top_repeat_customers = (
    customer_analysis[
        customer_analysis["Customer_Type"]
        == "Repeat Customer"
    ]
    .sort_values(
        by="Total_Orders",
        ascending=False
    )
    .head(10)
)

print("\n========== TOP 10 REPEAT CUSTOMERS ==========")
print(top_repeat_customers)


# ============================================================
# STEP 12 - TOP 10 CUSTOMERS BY REVENUE
# ============================================================

top_revenue_customers = (
    customer_analysis
    .sort_values(
        by="Total_Revenue",
        ascending=False
    )
    .head(10)
)

print("\n========== TOP 10 CUSTOMERS BY REVENUE ==========")
print(top_revenue_customers)


# ============================================================
# STEP 13 - COUNTRY ANALYSIS
# ============================================================

country_analysis = (
    df.groupby("Country")
    .agg(
        Customers=("CustomerID", "nunique"),
        Orders=("InvoiceNo", "nunique"),
        Revenue=("Revenue", "sum")
    )
    .reset_index()
    .sort_values(
        by="Revenue",
        ascending=False
    )
)

print("\n========== COUNTRY ANALYSIS ==========")
print(country_analysis)


# ============================================================
# STEP 14 - MONTHLY SALES
# ============================================================

df["Month"] = df["InvoiceDate"].dt.to_period("M")

monthly_sales = (
    df.groupby("Month")["Revenue"]
    .sum()
    .reset_index()
)

monthly_sales["Month"] = (
    monthly_sales["Month"].astype(str)
)

print("\n========== MONTHLY SALES ==========")
print(monthly_sales)


# ============================================================
# STEP 15 - SAVE CUSTOMER ANALYSIS
# ============================================================

customer_analysis.to_csv(
    "customer_analysis.csv",
    index=False
)

print("\nCustomer analysis saved successfully!")


# ============================================================
# STEP 19 - SAVE SEGMENT SUMMARY
# ============================================================

segment_summary.to_csv(
    "segment_summary.csv",
    index=False
)

print("Segment summary saved successfully!")


# ============================================================
# STEP 16 - SAVE COUNTRY ANALYSIS
# ============================================================

country_analysis.to_csv(
    "country_analysis.csv",
    index=False
)

print("Country analysis saved successfully!")


# ============================================================
# STEP 17 - SAVE MONTHLY SALES
# ============================================================

monthly_sales.to_csv(
    "monthly_sales.csv",
    index=False
)

print("Monthly sales saved successfully!")


# ============================================================
# STEP 18 - CUSTOMER TYPE CHART
# ============================================================

customer_type_counts = (
    customer_analysis["Customer_Type"]
    .value_counts()
)

plt.figure(figsize=(8, 5))

customer_type_counts.plot(
    kind="bar"
)

plt.title("First-time vs Repeat Customers")
plt.xlabel("Customer Type")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig(
    "first_time_vs_repeat_customers.png"
)

plt.show()


# ============================================================
# STEP 19 - CUSTOMER SEGMENT CHART
# ============================================================

segment_counts = (
    customer_analysis["Segment"]
    .value_counts()
)

plt.figure(figsize=(8, 5))

segment_counts.plot(
    kind="bar"
)

plt.title("Customer Segmentation")
plt.xlabel("Customer Segment")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig(
    "customer_segments.png"
)

plt.show()


# ============================================================
# STEP 20 - MONTHLY REVENUE CHART
# ============================================================

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_sales["Month"],
    monthly_sales["Revenue"],
    marker="o"
)

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "monthly_revenue_trend.png"
)

plt.show()


# ============================================================
# STEP 21 - TOP COUNTRIES BY REVENUE
# ============================================================

top_countries = country_analysis.head(10)

plt.figure(figsize=(10, 5))

plt.bar(
    top_countries["Country"],
    top_countries["Revenue"]
)

plt.title("Top 10 Countries by Revenue")
plt.xlabel("Country")
plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "top_countries_revenue.png"
)

plt.show()


# ============================================================
# STEP 22 - FINAL PROJECT SUMMARY
# ============================================================

print("\n")
print("==============================================")
print("       CUSTOMER REPEAT PURCHASE ANALYSIS")
print("==============================================")

print(
    "Total Customers:",
    total_customers
)

print(
    "First-time Customers:",
    first_time_customers
)

print(
    "Repeat Customers:",
    repeat_customers
)

print(
    "Repeat Purchase Rate:",
    round(repeat_purchase_rate, 2),
    "%"
)

print(
    "First-time Customer AOV:",
    round(first_time_aov, 2)
)

print(
    "Repeat Customer AOV:",
    round(repeat_aov, 2)
)

print("\nMost Common Customer Segment:")

print(
    customer_analysis["Segment"]
    .value_counts()
    .idxmax()
)

print("\n==============================================")
print("             ANALYSIS COMPLETED")
print("==============================================")
