# customer-repeat-purchase-analysis
Customer Repeat Purchase Analysis using Python, MySQL, Pandas, Matplotlib, and Excel. Analyzed first-time and repeat customers, repeat purchase rate, AOV, customer segmentation, revenue, orders, and purchasing trends.

Project title
Customer Repeat Purchase Analysis

📌 Project Overview

Customer Repeat Purchase Analysis is a data analytics project focused on understanding customer purchasing behavior.

The project analyzes transaction data to identify:

- First-time customers
- Repeat customers
- Repeat purchase rate
- Customer order frequency
- Average Order Value (AOV)
- Customer segments
- Customer revenue
- Country-wise performance
- Monthly revenue trends
- Top products and customers

The analysis was performed using “Python, Pandas, Matplotlib, MySQL, and Excel”.

🎯 Project Objective

The main objective of this project is to analyze customer purchase patterns and identify how frequently customers return to make additional purchases.

This analysis can help businesses understand customer retention and purchasing behavior.

 🛠️ Tools & Technologies

- Excel – Dataset preparation
- Python – Data analysis and visualization
- Pandas – Data manipulation
- Matplotlib – Data visualization
- MySQL – SQL-based data analysis
- GitHub – Project documentation and version control

📂 Dataset

The dataset contains retail transaction information.

Main Columns

| Column | Description |
|---|---|
| InvoiceNo | Unique invoice/order number |
| StockCode | Product code |
| Description | Product description |
| Quantity | Quantity purchased |
| InvoiceDate | Date and time of transaction |
| UnitPrice | Price per unit |
| CustomerID | Unique customer ID |
| Country | Customer's country |
| Revenue | Revenue generated from the transaction |

 🔄 Project Workflow

text
Excel Dataset
      ↓
Data Preparation
      ↓
Python Data Analysis
      ↓
Customer Order Analysis
      ↓
First-Time vs Repeat Customers
      ↓
Repeat Purchase Rate
      ↓
AOV Analysis
      ↓
Customer Segmentation
      ↓
MySQL Analysis
      ↓
Visualizations
      ↓
Business Insights

🐍 Python Analysis
Python was used to analyze customer purchasing behavior.
Key Analysis Performed
•	Loaded transaction dataset using Pandas 
•	Checked dataset structure 
•	Calculated total customers 
•	Calculated total orders 
•	Identified first-time customers 
•	Identified repeat customers 
•	Calculated repeat purchase rate 
•	Calculated customer revenue 
•	Calculated Average Order Value (AOV) 
•	Created customer segments 
•	Analyzed country-wise revenue
•	Analyzed monthly revenue 
•	Identified top customers 
•	Identified top products 

👥 Customer Classification
Customers were classified based on the number of distinct orders.
Orders	Customer Segment
1	One-time
2–3	Occasional
4–6	Regular
7+	Loyal
A customer with purchases across 2 or more distinct invoices is considered a repeat customer.

📊 Key Metrics
Repeat Purchase Rate 
Repeat Purchase Rate measures the percentage of customers who made two or more purchases.
Repeat Purchase Rate = (Repeat Customers / Total Customers) × 100
Average Order Value
AOV = Total Revenue / Total Orders
Revenue
Revenue = Quantity × Unit Price

🗄️ MySQL Analysis
MySQL was used for structured querying and business analysis.
The SQL analysis includes:
•	Total transactions 
•	Total customers 
•	Total orders 
•	Total revenue 
•	Total quantity sold 
•	Orders per customer 
•	First-time vs repeat customers 
•	Repeat purchase rate 
•	Customer revenue 
•	Average Order Value 
•	Customer segmentation 
•	Top repeat customers 
•	Top customers by revenue 
•	Country-wise revenue 
•	Monthly revenue 
•	Monthly orders 
•	Top products 
•	Highest order value 
________________________________________
📈 Visualizations
The Python analysis generated visualizations such as:
•	First-Time vs Repeat Customers 
•	Customer Segments 
•	Monthly Revenue Trend 
•	Top Countries by Revenue 
These charts help understand customer behavior and overall sales patterns.
________________________________________
💡 Business Insights
The project helps identify:
•	The proportion of customers who return for additional purchases 
•	Customer purchasing frequency 
•	High-value customers 
•	Customers who purchase only once 
•	Regular and loyal customer groups 
•	Countries contributing to revenue 
•	Monthly revenue patterns 
•	Products generating higher sales 
These insights can support customer retention and sales analysis.
________________________________________
📁 Project Structure
Customer-Repeat-Purchase-Analysis/
├── Customer_Repeat_Purchase_Analysis_Dataset.xlsx
├── customer_repeat_data.csv
│
├── customer repeat purchase.py
│
├── customer_analysis.csv
├── segment_summary.csv
├── country_analysis.csv
├── monthly_sales.csv
│
├── first_time_vs_repeat_customers.png
├── customer_segments.png
├── monthly_revenue_trend.png
├── top_countries_revenue.png
│
└── README.md

🚀 Future Scope
This project can be extended by adding:
•	Customer retention analysis 
•	Customer lifetime value analysis 
•	RFM analysis 
•	Customer churn analysis 
•	Sales forecasting 
•	Interactive Power BI dashboards 
•	Automated reporting 
________________________________________
🎓 Project Type
Data Analytics / Business Analytics Project
Technologies Used
Python Pandas Matplotlib MySQL Excel GitHub
________________________________________
👩‍💻 Author
Riddhi Shukla
BCA Student | Aspiring Data Analyst

