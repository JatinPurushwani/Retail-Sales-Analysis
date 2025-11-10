import pandas as pd
import numpy as np
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Retail Sales Analytics", layout="wide")

@st.cache_data
def load_data():
    p_csv = Path(__file__).resolve().parents[1] / "data" / "retail_sales.csv"
    df = pd.read_csv(p_csv, parse_dates=["Order_Date"])
    df["Profit_Margin"] = np.where(df["Sales"]>0, df["Profit"]/df["Sales"], 0.0)
    df["YearMonth"] = df["Order_Date"].dt.to_period("M").astype(str)
    return df

df = load_data()

st.title("Retail Sales Analytics Dashboard")
st.caption("Python · Pandas · Streamlit")

# Sidebar filters
with st.sidebar:
    st.header("Filters")
    years = sorted(df["Order_Date"].dt.year.unique().tolist())
    selected_years = st.multiselect("Year", years, default=years)
    regions = sorted(df["Region"].unique().tolist())
    selected_regions = st.multiselect("Region", regions, default=regions)
    categories = sorted(df["Category"].unique().tolist())
    selected_categories = st.multiselect("Category", categories, default=categories)

mask = (
    df["Order_Date"].dt.year.isin(selected_years)
    & df["Region"].isin(selected_regions)
    & df["Category"].isin(selected_categories)
)
fdf = df.loc[mask].copy()

# KPIs
total_sales = float(fdf["Sales"].sum())
total_profit = float(fdf["Profit"].sum())
avg_discount = float(fdf["Discount"].mean())
profit_margin = float((fdf["Profit"].sum() / fdf["Sales"].sum()) if fdf["Sales"].sum() > 0 else 0)

kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("Total Sales", f"${total_sales:,.0f}")
kpi2.metric("Total Profit", f"${total_profit:,.0f}")
kpi3.metric("Avg Discount", f"{avg_discount:.2%}")
kpi4.metric("Profit Margin", f"{profit_margin:.2%}")

# Trends and breakdowns
tab1, tab2, tab3, tab4 = st.tabs(["Monthly Trend", "Region", "Category", "Products"])

with tab1:
    st.subheader("Monthly Sales Trend")
    monthly = fdf.groupby("YearMonth", as_index=False)["Sales"].sum().sort_values("YearMonth")
    st.line_chart(monthly.set_index("YearMonth"))

with tab2:
    st.subheader("Profit by Region")
    region_profit = fdf.groupby("Region", as_index=False)["Profit"].sum().sort_values("Profit", ascending=False)
    st.bar_chart(region_profit.set_index("Region"))

with tab3:
    st.subheader("Category Contribution")
    cat_sales = fdf.groupby("Category", as_index=False)[["Sales","Profit"]].sum().sort_values("Sales", ascending=False)
    st.bar_chart(cat_sales.set_index("Category")[["Sales","Profit"]])

with tab4:
    st.subheader("Top 15 Sub-Categories by Sales")
    sub_top = fdf.groupby("Sub_Category", as_index=False)["Sales"].sum().sort_values("Sales", ascending=False).head(15)
    st.bar_chart(sub_top.set_index("Sub_Category"))

st.divider()
st.caption("Tip: Use the sidebar filters to drill down by year, region, and category.")
