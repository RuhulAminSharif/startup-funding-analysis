import streamlit as st 
import pandas as pd
from src.investor_comp import load_investor_details
from src.overall_comp import load_overall_analysis

@st.cache_data
def get_unique_investors(df):
  return sorted(df['investors'].str.split(',').explode().str.strip().unique().tolist())

if __name__ == "__main__":
  st.set_page_config(
    layout="wide",
    page_title="StartUp Analysis"
  )
  
  # Load Data
  df = pd.read_csv("data/cleaned_startup_data.csv")
  df["date"] = pd.to_datetime(df["date"])

  st.sidebar.title("Startup Funding Analysis")
  option = st.sidebar.selectbox("Select Analysis Type", ["Overall Analysis", "StartUp", "Investor"])

  if option == "Overall Analysis":
    st.title("Overall Analysis")
    load_overall_analysis(df)
      
  elif option == "StartUp":
    st.sidebar.subheader("Startup Search")
    startups = sorted(df["startup"].unique().tolist())
    selected_startup = st.sidebar.selectbox("Select StartUp", startups) 
    btn1 = st.sidebar.button("Find Startup Details")
    
    if btn1:
      st.title(f"Analysis for {selected_startup}")

  else:
    st.sidebar.subheader("Investor Search")
    investors_names = get_unique_investors(df)
    
    selected_investor = st.sidebar.selectbox("Select Investor", investors_names)
    btn2 = st.sidebar.button("Find Investor Details") 
    
    if btn2:
      load_investor_details(df, selected_investor)