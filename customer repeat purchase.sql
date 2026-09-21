CREATE DATABASE customer_repeat_analysis;

USE customer_repeat_analysis; 

CREATE TABLE retail_transactions (
    InvoiceNo VARCHAR(20),
    StockCode VARCHAR(20),
    Description VARCHAR(255),
    Quantity INT,
    InvoiceDate DATETIME,
    UnitPrice DECIMAL(10,2),
    CustomerID INT,
    Country VARCHAR(100),
    Revenue DECIMAL(12,2)
);

DESCRIBE retail_transactions;

USE customer_repeat_analysis;

SHOW TABLES;

SELECT COUNT(*) AS Total_Rows
FROM retail_transactions;

SELECT *
FROM retail_transactions
LIMIT 10;

SELECT COUNT(DISTINCT CustomerID) AS Total_Customers
FROM retail_transactions;

SELECT COUNT(DISTINCT InvoiceNo) AS Total_Orders
FROM retail_transactions;

SELECT ROUND(SUM(Revenue), 2) AS Total_Revenue
FROM retail_transactions;

SELECT SUM(Quantity) AS Total_Quantity
FROM retail_transactions;

SELECT
    CustomerID,
    COUNT(DISTINCT InvoiceNo) AS Total_Orders
FROM retail_transactions
GROUP BY CustomerID
ORDER BY Total_Orders DESC;

SELECT
    CustomerID,
    COUNT(DISTINCT InvoiceNo) AS Total_Orders,

    CASE
        WHEN COUNT(DISTINCT InvoiceNo) = 1
            THEN 'First-time Customer'
        ELSE 'Repeat Customer'
    END AS Customer_Type

FROM retail_transactions

GROUP BY CustomerID

ORDER BY Total_Orders DESC;

SELECT
    ROUND(
        100.0 *
        SUM(
            CASE
                WHEN Total_Orders >= 2 THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS Repeat_Purchase_Rate_Percent

FROM
(
    SELECT
        CustomerID,
        COUNT(DISTINCT InvoiceNo) AS Total_Orders

    FROM retail_transactions

    GROUP BY CustomerID
) AS Customer_Data;

SELECT COUNT(*) AS First_Time_Customers

FROM
(
    SELECT
        CustomerID,
        COUNT(DISTINCT InvoiceNo) AS Total_Orders

    FROM retail_transactions

    GROUP BY CustomerID
) AS Customer_Data

WHERE Total_Orders = 1;

SELECT COUNT(*) AS Repeat_Customers

FROM
(
    SELECT
        CustomerID,
        COUNT(DISTINCT InvoiceNo) AS Total_Orders

    FROM retail_transactions

    GROUP BY CustomerID
) AS Customer_Data

WHERE Total_Orders >= 2;

SELECT
    CustomerID,
    COUNT(DISTINCT InvoiceNo) AS Total_Orders,
    ROUND(SUM(Revenue), 2) AS Total_Revenue

FROM retail_transactions

GROUP BY CustomerID

ORDER BY Total_Revenue DESC;

SELECT
    ROUND(
        SUM(Revenue) / COUNT(DISTINCT InvoiceNo),
        2
    ) AS Overall_AOV

FROM retail_transactions;

SELECT
    Customer_Type,
    ROUND(AVG(AOV), 2) AS Average_AOV

FROM
(
    SELECT
        CustomerID,
        COUNT(DISTINCT InvoiceNo) AS Total_Orders,
        SUM(Revenue) AS Total_Revenue,

        SUM(Revenue) /
        COUNT(DISTINCT InvoiceNo) AS AOV,

        CASE
            WHEN COUNT(DISTINCT InvoiceNo) = 1
                THEN 'First-time Customer'
            ELSE 'Repeat Customer'
        END AS Customer_Type

    FROM retail_transactions

    GROUP BY CustomerID
) AS Customer_Data

GROUP BY Customer_Type;

SELECT
    CustomerID,
    Total_Orders,

    CASE
        WHEN Total_Orders = 1
            THEN 'One-time'

        WHEN Total_Orders BETWEEN 2 AND 3
            THEN 'Occasional'

        WHEN Total_Orders BETWEEN 4 AND 6
            THEN 'Regular'

        ELSE 'Loyal'
    END AS Customer_Segment

FROM
(
    SELECT
        CustomerID,
        COUNT(DISTINCT InvoiceNo) AS Total_Orders

    FROM retail_transactions

    GROUP BY CustomerID
) AS Customer_Data;

SELECT
    Customer_Segment,
    COUNT(*) AS Number_of_Customers

FROM
(
    SELECT
        CustomerID,
        CASE
            WHEN COUNT(DISTINCT InvoiceNo) = 1
                THEN 'One-time'

            WHEN COUNT(DISTINCT InvoiceNo) BETWEEN 2 AND 3
                THEN 'Occasional'

            WHEN COUNT(DISTINCT InvoiceNo) BETWEEN 4 AND 6
                THEN 'Regular'

            ELSE 'Loyal'
        END AS Customer_Segment

    FROM retail_transactions

    GROUP BY CustomerID
) AS Segments

GROUP BY Customer_Segment

ORDER BY Number_of_Customers DESC;

SELECT
    CustomerID,
    COUNT(DISTINCT InvoiceNo) AS Total_Orders,
    ROUND(SUM(Revenue), 2) AS Total_Revenue

FROM retail_transactions

GROUP BY CustomerID

HAVING COUNT(DISTINCT InvoiceNo) >= 2

ORDER BY Total_Orders DESC

LIMIT 10;

SELECT
    CustomerID,
    COUNT(DISTINCT InvoiceNo) AS Total_Orders,
    ROUND(SUM(Revenue), 2) AS Total_Revenue

FROM retail_transactions

GROUP BY CustomerID

ORDER BY Total_Revenue DESC

LIMIT 10;

SELECT
    Country,
    COUNT(DISTINCT CustomerID) AS Total_Customers,
    COUNT(DISTINCT InvoiceNo) AS Total_Orders,
    ROUND(SUM(Revenue), 2) AS Total_Revenue

FROM retail_transactions

GROUP BY Country

ORDER BY Total_Revenue DESC;

SELECT
    Country,
    ROUND(SUM(Revenue), 2) AS Total_Revenue

FROM retail_transactions

GROUP BY Country

ORDER BY Total_Revenue DESC

LIMIT 10;

SELECT
    DATE_FORMAT(InvoiceDate, '%Y-%m') AS Month,
    ROUND(SUM(Revenue), 2) AS Monthly_Revenue

FROM retail_transactions

GROUP BY DATE_FORMAT(InvoiceDate, '%Y-%m')

ORDER BY Month;

SELECT
    DATE_FORMAT(InvoiceDate, '%Y-%m') AS Month,
    COUNT(DISTINCT InvoiceNo) AS Total_Orders

FROM retail_transactions

GROUP BY DATE_FORMAT(InvoiceDate, '%Y-%m')

ORDER BY Month;

SELECT
    DATE_FORMAT(InvoiceDate, '%Y-%m') AS Month,
    COUNT(DISTINCT CustomerID) AS Total_Customers

FROM retail_transactions

GROUP BY DATE_FORMAT(InvoiceDate, '%Y-%m')

ORDER BY Month;

SELECT
    StockCode,
    Description,
    SUM(Quantity) AS Total_Quantity

FROM retail_transactions

GROUP BY StockCode, Description

ORDER BY Total_Quantity DESC

LIMIT 10;

SELECT
    StockCode,
    Description,
    ROUND(SUM(Revenue), 2) AS Total_Revenue

FROM retail_transactions

GROUP BY StockCode, Description

ORDER BY Total_Revenue DESC

LIMIT 10;

SELECT
    ROUND(
        SUM(Quantity) /
        COUNT(DISTINCT InvoiceNo),
        2
    ) AS Average_Quantity_Per_Order

FROM retail_transactions;

SELECT
    InvoiceNo,
    ROUND(SUM(Revenue), 2) AS Order_Value

FROM retail_transactions

GROUP BY InvoiceNo

ORDER BY Order_Value DESC

LIMIT 10;

SELECT
    ROUND(SUM(Revenue), 2) AS Repeat_Customer_Revenue

FROM retail_transactions

WHERE CustomerID IN
(
    SELECT CustomerID

    FROM retail_transactions

    GROUP BY CustomerID

    HAVING COUNT(DISTINCT InvoiceNo) >= 2
);

SELECT
    ROUND(SUM(Revenue), 2) AS First_Time_Customer_Revenue

FROM retail_transactions

WHERE CustomerID IN
(
    SELECT CustomerID

    FROM retail_transactions

    GROUP BY CustomerID

    HAVING COUNT(DISTINCT InvoiceNo) = 1
);

SELECT
    COUNT(DISTINCT CustomerID) AS Total_Customers,

    COUNT(DISTINCT InvoiceNo) AS Total_Orders,

    ROUND(SUM(Revenue), 2) AS Total_Revenue,

    SUM(Quantity) AS Total_Quantity,

    ROUND(
        SUM(Revenue) /
        COUNT(DISTINCT InvoiceNo),
        2
    ) AS Overall_AOV

FROM retail_transactions;

