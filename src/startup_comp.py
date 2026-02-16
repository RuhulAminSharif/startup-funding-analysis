import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_startup_analysis(df, startup_name):
  startup_df = df[df['startup'] == startup_name].copy()
  
  if startup_df.empty:
    st.error(f"No data found for {startup_name}")
    return

  st.title(f"Startup Profile: {startup_name}")
  
  # 1. KPI Metrics Row
  total_funding = startup_df['amount_crore_rs'].sum()
  sector = startup_df['vertical'].iloc[0] # Cleaned vertical
  city = startup_df['city'].iloc[0] # Cleaned city
  
  col1, col2, col3 = st.columns(3)
  col1.metric("Total Funding", f"₹{total_funding:.2f} Cr")
  col2.metric("Primary Sector", sector)
  col3.metric("Headquarters", city)

  st.divider()

  # 2. Funding History Table
  st.subheader("Funding History")
  history = startup_df[['date', 'round', 'investors', 'amount_crore_rs']].sort_values('date', ascending=False)
  history.columns = ["Date", "Round", "Investors", "Amount (Cr)"]
  st.dataframe(history, use_container_width=True)

  # 3. Growth Trajectory & Investor Pedigree
  col_a, col_b = st.columns(2)
  
  with col_a:
    st.subheader("Funding Trajectory")
    if len(startup_df) > 1:
      fig, ax = plt.subplots()
      ax.plot(startup_df['date'], startup_df['amount_crore_rs'], marker='o', linestyle='--')
      ax.set_ylabel("Amount in Crores")
      plt.xticks(rotation=45)
      st.pyplot(fig)
    else:
        st.info("Limited time-series data: This startup has only one recorded funding round.")

  with col_b:
    st.subheader("Investor List")
    # Exploding to get individual names if multiple investors joined a round
    investors = startup_df['investors'].str.split(',').explode().str.strip().unique()
    for inv in investors:
      st.markdown(f"- {inv}")

  st.divider()

  # 4. Competitive Benchmarking (Peer Analysis)
  st.subheader(f"Rank within {sector} Sector")
  
  # Get all startups in the same cleaned vertical
  peer_df = df[df['vertical'] == sector].groupby('startup')['amount_crore_rs'].sum().sort_values(ascending=False).head(10)
  
  fig2, ax2 = plt.subplots()
  # Highlight the current startup in a different color
  colors = ['#FF4B4B' if name == startup_name else '#1f77b4' for name in peer_df.index]
  ax2.barh(peer_df.index, peer_df.values, color=colors)
  ax2.invert_yaxis()
  ax2.set_xlabel("Total Funding (Cr)")
  st.pyplot(fig2)

  # 5. Local Context
  st.subheader(f"Funding Context in {city}")
  city_avg = df[df['city'] == city]['amount_crore_rs'].mean()
  startup_avg = startup_df['amount_crore_rs'].mean()
  
  if startup_avg > city_avg:
    st.success(f"{startup_name}'s average deal size is higher than the {city} city average of ₹{city_avg:.2f} Cr.")
  else:
    st.info(f"The average deal size in {city} is ₹{city_avg:.2f} Cr.")