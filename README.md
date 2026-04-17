# Sales-Profitability--Analysis--Dashboard
Interactive Streamlit dashboard for sales, profit, and cost analysis with Pareto insights and business recommendations.

Built using **Python, Pandas, Plotly, and Streamlit**.

Data Analytics Project | Streamlit Web App

 # Project Overview

This project presents a comprehensive analysis of sales, cost, and profitability for the Nassau Candy Distributor.

The goal is to uncover:

- True profit-driving products

- Cost inefficiencies

- Division-level performance gaps

- Revenue and profit concentration risks

An interactive Streamlit dashboard is developed to enable real-time insights and decision-making.

# Problem Statement

Traditional metrics like sales volume alone are misleading.

This project addresses key business challenges:

- Which products actually generate profit?

- Are high-sales products truly profitable?

- Which divisions are underperforming?

- Where are pricing and cost inefficiencies?

# Dataset Description:

The dataset includes:

- Product & division details

- Sales, cost, profit metrics

- Customer location & region

- Order & shipping data

- Factory mapping information

# Key Fields:

- Sales

- Cost

- Units

- Gross Profit

- Division

- Product Name


# Data Cleaning & Preprocessing

- Removed missing and invalid records

- Validated cost and sales values

- Standardized product/division labels

- Created derived metrics:

- Total Profit
- Gross Margin (%)
- Profit per Unit
  
# Exploratory Data Analysis (EDA)
🔍 Key Analysis Performed:

- Product-level profitability ranking
- Division-level performance comparison
- Cost vs Sales diagnostics
- Pareto (80–20) analysis

# Key Insights

- A small number of products drive most revenue and profit

- Several high-sales products have low margins (pricing issues)

- Cost-heavy products reduce overall profitability

- Division performance varies significantly

# Business Recommendations
- Increase focus on high-margin products

- Optimize cost through supplier negotiation

- Reprice high-demand low-margin products

- Reduce dependency on top-performing products

- Remove or improve low-performing products

# Dashboard Features (Streamlit)
🧩 Modules

- Product Profitability Overview

- Division Performance Dashboard

- Cost vs Margin Diagnostics

- Pareto Analysis

🎛 User Controls

- Date range filter

- Division filter

- Margin threshold slider

- Product search
  
🚀 Live Demo

👉 Streamlit App:
🔗https://sales-profitability--analysis--dashboard-gk86wdsqe89trrq5zmrea.streamlit.app/

💻 How to Run Locally
```bash
# Clone repository
git clone https://github.com/your-username/your-repo-name.git

# Navigate to folder
cd your-repo-name

# Install dependencies
pip install -r requirements.txt

# Run app
python -m streamlit run app.py
```
# Project Structure
```bash
📦 project-folder
 ┣ 📜 app.py
 ┣ 📜 data.csv
 ┣ 📜 requirements.txt
 ┣ 📜 README.md
 ┣ 📂 reports
 ┃ ┗ 📄 research_paper.pdf
```
# Requirements
```bash
streamlit
pandas
matplotlib
seaborn
```
# Deliverables

- Research Paper (EDA, insights, recommendations)
- Streamlit Dashboard
- Business Insights & KPI Analysis

# Key KPIs
- Gross Margin (%)
- Profit per Unit
- Revenue Contribution
- Profit Contribution
- Margin Volatility
# Future Improvements
- Add real-time data integration
- Advanced forecasting models
- Supply chain optimization analytics
- Deployment on cloud platforms
# Acknowledgements

This project was developed as part of a data analytics and business intelligence exercise to demonstrate real-world problem-solving using data.
