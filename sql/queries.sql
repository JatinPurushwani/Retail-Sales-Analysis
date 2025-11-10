-- Retail Sales Analytics: Core Queries

-- 1) Monthly Sales Trend
SELECT strftime('%Y-%m', Order_Date) AS Month, SUM(Sales) AS Monthly_Sales
FROM Retail_Sales
GROUP BY Month
ORDER BY Month;

-- 2) Regional Profit Performance
SELECT Region, ROUND(SUM(Profit),2) AS Total_Profit
FROM Retail_Sales
GROUP BY Region
ORDER BY Total_Profit DESC;

-- 3) Top Sub-Categories by Sales
SELECT Sub_Category, ROUND(SUM(Sales),2) AS Total_Sales
FROM Retail_Sales
GROUP BY Sub_Category
ORDER BY Total_Sales DESC
LIMIT 10;

-- 4) Category Contribution
SELECT Category, ROUND(SUM(Sales),2) AS Sales, ROUND(SUM(Profit),2) AS Profit
FROM Retail_Sales
GROUP BY Category
ORDER BY Sales DESC;

-- 5) Discount Impact on Profit (binned)
SELECT CASE
         WHEN Discount < 0.05 THEN '<5%'
         WHEN Discount < 0.10 THEN '5-10%'
         WHEN Discount < 0.20 THEN '10-20%'
         WHEN Discount < 0.30 THEN '20-30%'
         ELSE '>=30%'
       END AS Discount_Bin,
       ROUND(AVG(Profit),2) AS Avg_Profit
FROM Retail_Sales
GROUP BY Discount_Bin
ORDER BY Discount_Bin;
