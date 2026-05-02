import streamlit as st
import pandas as pd

st.title("ApexPlanet Sales Dashboard 🎀")
df = pd.read_parquet('data/processed/clean_sales.parquet')

st.line_chart(df.set_index('timestamp')['sales_amount'])
st.write("Cleaned and validated by the ApexPlanet ETL Pipeline.")