# Retail Sales Analytics – Python · SQL · Streamlit

End-to-end analytics project: synthetic retail sales data, SQL queries, Python EDA, and an interactive Streamlit dashboard.

## Features
- 12,000 orders across 2 years
- KPIs: Total Sales, Profit, Profit Margin, Avg Discount
- SQL: monthly trend, regional profit, top sub-categories, discount impact
- Streamlit dashboard with filters and charts
- Notebook for EDA and insights
- SQLite ETL script (optional)

## Structure
```
retail-sales-analytics/
├─ app/
│  └─ streamlit_app.py
├─ data/
│  └─ retail_sales.csv
├─ notebooks/
│  └─ 01_eda.ipynb
├─ sql/
│  └─ queries.sql
├─ src/
│  └─ etl.py
└─ requirements.txt
```

## Quickstart
```bash
# 1) Create and activate a venv (recommended)
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

# 2) Install deps
pip install -r requirements.txt

# 3) Run the Streamlit app
streamlit run app/streamlit_app.py
```

## Optional: Load into SQLite
```bash
python src/etl.py
```

## Deployment (Streamlit Community Cloud)
- Push this repo to GitHub.
- In Streamlit Cloud, select the repo and set the file path to `app/streamlit_app.py`.
- Add `data/retail_sales.csv` to the repo so the app has data at runtime.

## Resume line
**Retail Sales Analytics Dashboard – Python | SQL | Streamlit**  
Built an interactive analytics dashboard on 12K+ orders across 2 years. Implemented SQL queries and Python EDA to identify revenue drivers, margin impacts, and regional trends. Delivered KPIs and insights with a Streamlit dashboard.
