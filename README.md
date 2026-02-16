# Startup Funding Analysis Dashboard

A comprehensive data analysis dashboard built with **Streamlit** to explore and visualize the Indian startup ecosystem. This project transforms raw, fragmented investment data into actionable insights through rigorous data cleaning and interactive visualizations.

## 🚀 Live Demo

The application is live and can be accessed here: **[StartUp-Funding-Analysis](https://startup-funding-analysis-app.streamlit.app/)**


## 📊 Key Features

The dashboard is divided into three specialized analytical modules, each providing unique insights into the Indian startup ecosystem.

### 1. Overall Ecosystem Analysis (Macro View)

Gain a high-level perspective of market trends and dominant players across the country.

* **Real-time KPI Metrics**: Instant visibility into total investment value, maximum funding amounts, average ticket sizes, and total startup counts.
* **Interactive MoM Trends**: A toggleable Month-on-Month analysis to track either **Total Funding Amount** or **Deal Count** over time.
* **Geographical & Sectoral Insights**:
  * **Top 10 Sectors**: Horizontal bar charts identifying industries attracting the most capital.
  * **Top 10 Cities**: Identification of regional funding hubs (e.g., Bengaluru, Mumbai, NCR).


* **Ecosystem Leaderboards**: Dedicated tabs for the most funded startups and the most active investors based on total deal volume.

### 2. Investor Insights (Portfolio View)

Deep-dive into the strategies and portfolios of specific investment firms or individuals.

* **Investor Performance Metrics**: Quick summary of total capital deployed and the number of unique startups supported.
* **Portfolio Breakdown**:
  * **Recent Activity**: A detailed table of the five most recent investments.
  * **Biggest Bets**: Bar charts highlighting the startup names where the investor has the highest financial exposure.


* **Strategic Distribution**: Interactive pie charts visualizing the investor's preference across different **Sectors**, **Cities**, and **Investment Rounds**.
* **Network Analysis (Co-investors)**: Identification of frequent investment partners by analyzing shared deal history.
* **Year-on-Year Growth**: A line graph tracking the investor's capital deployment trajectory over the years.

### 3. Startup Analysis (Company View)

Analyze the individual funding lifecycle and competitive standing of specific startups.

* **Company Snapshot**: High-level summary of a startup’s total capital raised, primary vertical, and headquarters.
* **Funding History**: A chronological, detailed list of all recorded funding rounds, including dates, investment types, and participating backers.
* **Growth Trajectory**: A time-series visualization of funding rounds to track increase in check sizes over time.
* **Investor Pedigree**: An exploded list of all unique investors who have ever backed the company.
* **Competitive Benchmarking**:
* **Sector Ranking**: A localized leaderboard ranking the selected startup against the Top 10 peers in its specific vertical.
* **City Context**: Automated comparison of the startup’s average deal size against its city's overall market average.


## 🛠️ The Data Engineering Challenge

One of the primary focuses of this project was the **Data Cleaning Pipeline**. Raw startup data is notoriously messy; this project implements:

* **Vertical Standardization**: Unified over 50+ fragmented sectors (e.g., merging "E-commerce", "Ecommerce", and "E-tailer").
* **City Normalization**: Corrected variations like "Bangalore" to "Bengaluru" and "Gurgaon" to "Gurugram" to ensure geographical accuracy.
* **Date Uniformity**: Resolved  parsing errors to enable accurate time-series analysis.
* **Amount Conversion**: Standardized all funding values into "Crore INR" for consistent mathematical operations.


## 💻 Tech Stack

* **Language**: Python
* **Web Framework**: Streamlit
* **Data Manipulation**: Pandas, NumPy
* **Visualization**: Matplotlib
* **Deployment**: Streamlit Cloud


## 📂 Project Structure

```text
├── data/
│   └── cleaned_startup_data.csv   # Pre-processed dataset
├── src/
│   ├── investor_comp.py           # Investor analysis logic
│   ├── startup_comp.py            # Startup profile logic
│   └── overall_comp.py            # Macro ecosystem analysis
├── main.py                        # Entry point & Sidebar logic
└── requirements.txt               # Dependencies

```


## 🔧 Installation & Local Setup

1. **Clone the repository**
```bash
git clone https://github.com/RuhulAminSharif/startup-funding-analysis.git
cd startup-funding-analysis

```


2. **Install dependencies**
```bash
pip install -r requirements.txt

```


3. **Run the App**
```bash
streamlit run main.py

```


## 👨‍💻 Author

**Ruhul Amin Sharif**  
B.Sc. in Computer Science and Engineering  
Premier University, Chattogram


