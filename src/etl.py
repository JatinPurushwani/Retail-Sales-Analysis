import pandas as pd
import sqlite3
from pathlib import Path

def load_to_sqlite(csv_path: str, db_path: str = "retail_sales.db", table_name: str = "Retail_Sales"):
    df = pd.read_csv(csv_path, parse_dates=["Order_Date"])
    # enforce dtypes
    df["Order_ID"] = df["Order_ID"].astype(str)
    df["Customer_ID"] = df["Customer_ID"].astype(str)
    df["Customer_Name"] = df["Customer_Name"].astype(str)
    df["Region"] = df["Region"].astype(str)
    df["Category"] = df["Category"].astype(str)
    df["Sub_Category"] = df["Sub_Category"].astype(str)
    df["Sales"] = df["Sales"].astype(float)
    df["Quantity"] = df["Quantity"].astype(int)
    df["Discount"] = df["Discount"].astype(float)
    df["Profit"] = df["Profit"].astype(float)

    con = sqlite3.connect(db_path)
    df.to_sql(table_name, con, if_exists="replace", index=False)
    con.close()
    print(f"Loaded {len(df)} rows into {db_path}:{table_name}")

if __name__ == "__main__":
    load_to_sqlite("data/retail_sales.csv")
