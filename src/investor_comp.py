import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- HELPER FUNCTIONS ---

def plot_pie(values, index, title):
  """Generic helper to plot consistent pie charts"""
  if values.empty:
    st.write(f"No data available for {title}")
    return
  
  fig, ax = plt.subplots()
  ax.pie(values, labels=index, autopct="%0.1f%%", startangle=140)
  st.subheader(title)
  st.pyplot(fig)

# --- ANALYSIS FUNCTIONS ---

def recent_five_investments(investments):
  st.subheader("Most Recent Investments")
  # Select and rename for display
  last5 = investments.head(5)[
    ["date", "startup", "vertical", "city", "round", "amount_crore_rs"]
  ].copy()
  
  last5.rename(columns={
    'date': 'Date',
    'startup': 'Startup Name',
    'city': 'City',
    'vertical': 'Vertical',
    'round': 'Investment Type',
    'amount_crore_rs': "Amount (Cr)"
  }, inplace=True)
  
  # Handle zeros for display
  last5["Amount (Cr)"] = last5["Amount (Cr)"].replace(0, "Unknown")
  st.dataframe(last5, use_container_width=True)

def plot_biggest_investment(investments):
  st.subheader("Biggest Investments")
  big_investments = (investments.groupby('startup')['amount_crore_rs']
                      .sum()
                      .sort_values(ascending=False)
                      .head(5))
  
  if big_investments.empty or big_investments.sum() == 0:
    st.info("No investment amount data available for this investor.")
    return

  fig, ax = plt.subplots()
  ax.bar(big_investments.index, big_investments.values, color='#1f77b4')
  plt.xticks(rotation=45)
  ax.set_ylabel("Amount in Crores")
  st.pyplot(fig)

def plot_YoY(investments):
  st.subheader("Year-on-Year Investment Trend")
  yoy_data = (investments.groupby(investments["date"].dt.year)['amount_crore_rs']
              .sum())
  
  if yoy_data.empty:
    st.write("No yearly data found.")
    return

  fig, ax = plt.subplots()
  ax.plot(yoy_data.index, yoy_data.values, marker='o', linestyle='-', linewidth=2)
  ax.set_xticks(yoy_data.index.astype(int))
  ax.set_ylabel("Amount (Crore Rs)")
  st.pyplot(fig)

def plot_co_investors(investor_df, current_investor):
  st.subheader("Top Co-investors")
  all_investors = investor_df['investors'].str.split(',').explode().str.strip()
  partners = all_investors[all_investors.str.lower() != current_investor.lower()]
  partner_counts = partners.value_counts().head(5)
  
  if not partner_counts.empty:
    fig, ax = plt.subplots()
    partner_counts.plot(kind='barh', ax=ax, color='#ff7f0e')
    ax.set_xlabel("Number of Shared Deals")
    st.pyplot(fig)
  else:
    st.write("This investor usually invests alone.")

# --- MAIN LOADER ---

def load_investor_details(df, investor):
  investor_df = df[df['investors'].str.contains(investor, na=False, case=False)].copy()
  
  if investor_df.empty:
    st.error(f"No records found for '{investor}'")
    return

  st.title(f"Investor Profile: {investor}")

  total_invested = investor_df['amount_crore_rs'].sum()
  num_startups = investor_df['startup'].nunique()
  
  m1, m2 = st.columns(2)
  m1.metric("Total Invested", f"₹{total_invested:.2f} Cr")
  m2.metric("Startups Funded", num_startups)
  
  st.divider()

  recent_five_investments(investor_df)
  
  st.divider()

  col1, col2 = st.columns(2)
  with col1:
    plot_biggest_investment(investor_df)
  with col2:
    verticals = investor_df.groupby("vertical")["amount_crore_rs"].sum()
    plot_pie(verticals, verticals.index, "Sectors Invested In")
  
  st.divider()

  col3, col4 = st.columns(2)
  with col3:
    city_data = investor_df.groupby('city')['amount_crore_rs'].sum()
    plot_pie(city_data, city_data.index, "City Distribution")
  with col4:
    type_data = investor_df.groupby('round')['amount_crore_rs'].sum()
    plot_pie(type_data, type_data.index, "Investment Rounds")
  
  st.divider()
  
  plot_YoY(investor_df)

  plot_co_investors(investor_df, investor)