# Power BI Setup Guide for Retail Sales Analytics

This guide explains how to build the Power BI dashboard using the same dataset (`retail_sales.csv`).

## KPIs to Include
1. **Total Sales** = SUM(Sales)
2. **Total Profit** = SUM(Profit)
3. **Average Discount** = AVERAGE(Discount)
4. **Profit Margin** = DIVIDE(SUM(Profit), SUM(Sales))
5. **Total Quantity Sold** = SUM(Quantity)

## Recommended Visuals
| Visual | Fields | Description |
|--------|---------|-------------|
| **Card Visuals** | Total Sales, Total Profit, Avg Discount, Profit Margin | Top KPIs at a glance |
| **Line Chart** | Axis: Order_Date (Month), Values: SUM(Sales) | Monthly sales trend |
| **Clustered Bar Chart** | Axis: Region, Values: SUM(Profit) | Regional profit distribution |
| **Stacked Column Chart** | Axis: Category, Values: SUM(Sales), Legend: Region | Category contribution by region |
| **Donut Chart** | Values: SUM(Sales), Legend: Category | Share of sales by category |
| **Table / Matrix** | Sub_Category, SUM(Sales), SUM(Profit), AVERAGE(Discount) | Product-level insight |
| **Slicer Filters** | Region, Category, Order_Date | Interactive filters |

## Additional Calculated Columns (Optional)
1. `Year` = YEAR('Retail_Sales'[Order_Date])
2. `Month` = FORMAT('Retail_Sales'[Order_Date], "MMM YYYY")

## Steps
1. Open **Power BI Desktop**.
2. Click **Get Data → Text/CSV**, and import `retail_sales.csv`.
3. In the **Data view**, verify the data types (ensure Order_Date is recognized as Date).
4. Create the above KPIs in **Modeling → New Measure**.
5. Add visuals to the report canvas using the fields as per the table above.
6. Format visuals (use consistent colors for Sales vs Profit).
7. Add slicers on **Region** and **Category** to enable drill-downs.
8. Save as `retail_sales_dashboard.pbix`.

## Recommended Layout
| Section | Contents |
|----------|-----------|
| Header | Project title + date filters |
| Top row | KPI cards |
| Middle row | Trend (line chart) + Region (bar chart) |
| Bottom row | Category/Sub-category visuals + Table |

---

**Deliverables:**
- Power BI report file: `retail_sales_dashboard.pbix`
- Dataset: `retail_sales.csv` (already provided)
