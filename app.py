import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_style("whitegrid")

st.set_page_config(layout="wide")

st.title("📊 Profitability & Performance Dashboard")

# -----------------------------
# LOAD DATA
# -----------------------------
data = pd.read_csv(r"C:\Users\lenovo\OneDrive\picture 2\python series\Nassau Candy Distributor.csv")

# -----------------------------
# PREPROCESSING
# -----------------------------
data['Total_Profit'] = data['Sales'] - data['Cost']
data['Gross Margin'] = (data['Total_Profit'] / data['Sales']) * 100

# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
st.sidebar.header("🔍 Filters")

# Division Filter
division = st.sidebar.multiselect(
    "Select Division",
    options=data['Division'].unique(),
    default=data['Division'].unique()
)

# Margin Slider
margin_threshold = st.sidebar.slider(
    "Minimum Margin (%)",
    float(data['Gross Margin'].min()),
    float(data['Gross Margin'].max()),
    0.0
)

# Product Search
product_search = st.sidebar.text_input("Search Product")

# Apply filters
filtered_data = data[
    (data['Division'].isin(division)) &
    (data['Gross Margin'] >= margin_threshold)
]

if product_search:
    filtered_data = filtered_data[
        filtered_data['Product Name'].str.contains(product_search, case=False)
    ]


data['Order Date'] = pd.to_datetime(data['Order Date'], dayfirst=True)

date_range = st.sidebar.date_input("Select Date Range", [])

if len(date_range) == 2:
    filtered_data = filtered_data[
        (filtered_data['Order Date'] >= pd.to_datetime(date_range[0])) &
        (filtered_data['Order Date'] <= pd.to_datetime(date_range[1]))
    ]

# -----------------------------
# 📊 MODULE 1: PRODUCT PROFITABILITY
# -----------------------------
st.header("📦 Product Profitability Overview")

top_products = filtered_data.sort_values(by='Gross Margin', ascending=False).head(10)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Margin Leaderboard")
    st.dataframe(top_products[['Product Name', 'Gross Margin', 'Total_Profit']])

with col2:
    st.subheader("Profit Contribution")

    fig, ax = plt.subplots()
    ax.bar(top_products['Product Name'], top_products['Total_Profit'])
    plt.xticks(rotation=45)
    st.pyplot(fig)

# -----------------------------
# 📊 MODULE 2: DIVISION PERFORMANCE
# -----------------------------
st.header("🏢 Division Performance")

df_div = filtered_data.groupby('Division').agg({
    'Sales': 'sum',
    'Total_Profit': 'sum',
    'Gross Margin': 'mean'
}).reset_index()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Revenue vs Profit")

    fig, ax = plt.subplots()
    ax.bar(df_div['Division'], df_div['Sales'], label="Revenue")
    ax.bar(df_div['Division'], df_div['Total_Profit'], label="Profit")
    plt.xticks(rotation=45)
    ax.legend()
    st.pyplot(fig)

with col2:
    st.subheader("Margin Distribution")

    fig, ax = plt.subplots()
    sns.barplot(x='Division', y='Gross Margin', data=df_div, ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# -----------------------------
# 📊 MODULE 3: COST DIAGNOSTICS
# -----------------------------
st.header("💸 Cost vs Margin Diagnostics")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Cost vs Sales")

    fig, ax = plt.subplots()
    sns.scatterplot(x='Cost', y='Sales', data=filtered_data, ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("Margin Risk Flags")

    risk_data = filtered_data[
        (filtered_data['Cost'] > filtered_data['Cost'].mean()) &
        (filtered_data['Gross Margin'] < filtered_data['Gross Margin'].mean())
    ]

    st.dataframe(risk_data[['Product Name', 'Cost', 'Gross Margin']])

# -----------------------------
# 📊 MODULE 4: PARETO ANALYSIS
# -----------------------------
st.header("📈 Profit Concentration (Pareto)")

data_sorted = filtered_data.sort_values(by='Sales', ascending=False).reset_index(drop=True)
data_sorted['cum_sales_pct'] = data_sorted['Sales'].cumsum() / data_sorted['Sales'].sum() * 100

fig, ax = plt.subplots()

ax.bar(range(len(data_sorted)), data_sorted['Sales'])
ax.plot(range(len(data_sorted)), data_sorted['cum_sales_pct'])
ax.axhline(y=80)

st.pyplot(fig)

# Dependency indicator
top_80 = data_sorted[data_sorted['cum_sales_pct'] <= 80]

st.subheader("Dependency Indicator")

st.write(f"{len(top_80)} products contribute to 80% of revenue")

if len(top_80) < 0.2 * len(data_sorted):
    st.warning("⚠ High dependency on few products!")
else:
    st.success("✅ Balanced product contribution")