import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import openpyxl as pxl

# Display the logo
st.image(r"C:\Users\kinda\OneDrive\Desktop\Logo coffee analysis.jpg", use_container_width=False, width=130)

# App title
st.title("☕️ Coffee Sales Analysis App")
st.sidebar.title("📊 Input Options")

# Upload the data
uploaded_file = st.sidebar.file_uploader("Upload your Coffee Sales Data", type=["xlsx", "csv"])
if uploaded_file is not None:
    # Load data based on file type
    if uploaded_file.name.endswith(".xlsx"):
        data = pd.read_excel(uploaded_file)
    else:
        data = pd.read_csv(uploaded_file)

    # Clean column names
    data.columns = data.columns.str.strip()

    # Data preview
    st.subheader("🔍 Data Preview")
    st.dataframe(data.head())
# Removed misplaced string literal


    # Missing data check
    st.subheader("⚠️ Missing Data Overview")
    st.write(data.isnull().sum())

    # Choose analysis
    analysis_type = st.sidebar.selectbox(
        "Choose Analysis Type",
        ["Sales by Store Location", "Most Popular Products", "Organic Coffee Analysis", "Eco-Friendly Cups Analysis", "Price vs Quantity (Matplotlib)", "Price Distribution (Histogram)"]
    )

    # 1. Sales by Store Location
    if analysis_type == "Sales by Store Location":
        if 'Store_location' in data.columns:
            store_counts = data['Store_location'].value_counts()
            st.subheader("🗺 Sales by Store Location")
            st.bar_chart(store_counts)
        else:
            st.error("❌ 'Store_location' column is missing.")

    # 2. Most Popular Products
    elif analysis_type == "Most Popular Products":
        if 'Product_type' in data.columns:
            top_products = data['Product_type'].value_counts().head(5)
            st.subheader("🏆 Top 5 Most Popular Products")
            st.bar_chart(top_products)
        else:
            st.error("❌ 'Product_type' column is missing.")

    # 3. Organic Coffee Analysis
    elif analysis_type == "Organic Coffee Analysis":
        if 'Organic Coffee' in data.columns:
            organic_counts = data['Organic Coffee'].value_counts()
            fig = px.pie(
                names=organic_counts.index,
                values=organic_counts.values,
                title="🌱 Organic Coffee Distribution"
            )
            st.plotly_chart(fig)
        else:
            st.error("❌ 'Organic Coffee' column is missing.")

    # 4. Eco-Friendly Cups
    elif analysis_type == "Eco-Friendly Cups Analysis":
        if 'Eco -Friendly cup' in data.columns:
            eco_counts = data['Eco -Friendly cup'].value_counts()
            fig = px.pie(
                names=eco_counts.index,
                values=eco_counts.values,
                title="♻️ Eco-Friendly Cups Usage"
            )
            st.plotly_chart(fig)
        else:
            st.error("❌ 'Eco -Friendly cup' column is missing.")

    # 5. Scatter Plot: Price vs Quantity using Matplotlib
    elif analysis_type == "Price vs Quantity (Matplotlib)":
        if 'Unit_price' in data.columns and 'Transaction_qty' in data.columns:
            st.subheader("📈 Price vs Quantity Scatter Plot (Matplotlib)")
            fig, ax = plt.subplots()
            ax.scatter(data['Unit_price'], data['Transaction_qty'], color='green', alpha=0.6)
            ax.set_xlabel("Unit Price")
            ax.set_ylabel("Transaction Quantity")
            ax.set_title("Unit Price vs Quantity Sold")
            st.pyplot(fig)
        else:
            st.error("❌ 'Unit_price' and/or 'Transaction_qty' columns are missing.")
# 6. Histogram: Unit Price
    elif analysis_type == "Price Distribution (Histogram)":
        if 'Unit_price' in data.columns:
            st.subheader("📊 Price Distribution Histogram")

        # Drop missing values
        unit_prices = data['Unit_price'].dropna()

        # Create histogram
        fig, ax = plt.subplots()
        counts, bins, patches = ax.hist(unit_prices, bins=20, color='skyblue', edgecolor='black')

        # Set axis labels and title
        ax.set_xlabel("Unit Price")
        ax.set_ylabel("Frequency")
        ax.set_title("Distribution of Unit Prices")

        # Create custom x-tick labels at bin centers
        bin_centers = 0.5 * (bins[1:] + bins[:-1])
        ax.set_xticks(bin_centers)
        ax.set_xticklabels([f"{int(b)}" for b in bin_centers], rotation=45)

        # Optional: Annotate each bar with count
        for count, patch in zip(counts, patches):
            height = patch.get_height()
            if height > 0:
                ax.text(patch.get_x() + patch.get_width() / 2, height + 1, str(int(count)),
                        ha='center', va='bottom', fontsize=8)

        st.pyplot(fig)
    else:
        st.error("❌ 'Unit_price' column is missing.")


    # 7. Revenue Calculation
    if st.sidebar.checkbox("💰 Calculate Revenue"):
        if 'Transaction_qty' in data.columns and 'Unit_price' in data.columns and 'Product_type' in data.columns:
            data['Revenue'] = data['Transaction_qty'] * data['Unit_price']
            st.subheader("💵 Revenue Preview")
            st.dataframe(data[['Product_type', 'Revenue']].head())

            revenue_summary = data.groupby('Product_type')['Revenue'].sum().sort_values(ascending=False)
            st.subheader("📌 Revenue by Product")
            st.bar_chart(revenue_summary)
        else:
            st.error("❌ Columns 'Transaction_qty', 'Unit_price', or 'Product_type' are missing.")
else:
    st.info("📂 Please upload a data file to begin analysis.")
