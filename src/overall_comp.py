import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_kpi_metrics(df):
  total_funding = df['amount_crore_rs'].sum()
  max_funding = df['amount_crore_rs'].max()
  avg_funding = df['amount_crore_rs'].mean()
  num_startups = df['startup'].nunique()

  col1, col2, col3, col4 = st.columns(4)
  col1.metric("Total Investment", f"₹{total_funding:,.0f} Cr")
  col2.metric("Max Funding", f"₹{max_funding:,.0f} Cr")
  col3.metric("Avg Ticket Size", f"₹{avg_funding:,.2f} Cr")
  col4.metric("Total Startups", num_startups)

def MoM_analysis(df):
  st.subheader("Month-on-Month Analysis")
  selected_option = st.selectbox("Select Metric", ["Total Amount", "Deal Count"])
  
  temp_df = df.copy()
  temp_df['month_year'] = temp_df['date'].dt.to_period('M').astype(str)
  
  if selected_option == "Total Amount":
    mom_data = temp_df.groupby('month_year')['amount_crore_rs'].sum().reset_index()
  else:
    mom_data = temp_df.groupby('month_year')['amount_crore_rs'].count().reset_index()

  fig, ax = plt.subplots(figsize=(12, 5))
  ax.plot(mom_data['month_year'], mom_data['amount_crore_rs'], marker='o', color='#2ca02c')
  plt.xticks(rotation=90)
  ax.set_ylabel(selected_option)
  st.pyplot(fig)

def sector_analysis(df):
  top_sectors = df.groupby('vertical')['amount_crore_rs'].sum().sort_values(ascending=False).head(10)
  fig_sec, ax_sec = plt.subplots()
  ax_sec.barh(top_sectors.index, top_sectors.values, color='skyblue')
  ax_sec.invert_yaxis()
  st.pyplot(fig_sec)

def city_analysis(df):
  top_cities = df.groupby('city')['amount_crore_rs'].sum().sort_values(ascending=False).head(10)
  fig_city, ax_city = plt.subplots()
  ax_city.barh(top_cities.index, top_cities.values, color='salmon')
  ax_city.invert_yaxis()
  st.pyplot(fig_city)

def top_startups_analysis(df):
  top_startups = df.groupby('startup')['amount_crore_rs'].sum().sort_values(ascending=False).head(10).reset_index()
  top_startups.columns = ["Startup Name", "Total Funding (Cr)"]
  st.table(top_startups) 
  
def top_investors_analysis(df):
  investor_series = df['investors'].str.split(',').explode().str.strip()
  top_investors = investor_series.value_counts().head(10).reset_index()
  top_investors.columns = ["Investor Name", "Deal Count"]
  st.table(top_investors)

def load_overall_analysis(df):

  show_kpi_metrics(df)
  st.divider()

  MoM_analysis(df)
  st.divider()


  col1, col2 = st.columns(2)

  with col1:
    st.subheader("Top Sectors (by Amount)")
    sector_analysis(df)

  with col2:
    st.subheader("Top Cities (by Amount)")
    city_analysis(df)

  st.divider()

  st.subheader("Ecosystem Leaderboards")
  tab1, tab2 = st.tabs(["Top Startups", "Top Investors"])

  with tab1:
    top_startups_analysis(df)

  with tab2:
    top_investors_analysis(df)