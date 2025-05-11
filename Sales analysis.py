import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt


# Display the logo
st.image(r"C:\Users\kinda\OneDrive\Desktop\Logo coffee analysis.jpg", use_container_width=False, width=130)

# App title
st.title("📊 Sales Analysis App")
st.sidebar.title("📂 Input Options")

# Upload the data
uploaded_file = st.sidebar.file_uploader("Upload your Sales Data", type=["xlsx", "csv"])
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

    # Missing data check
    st.subheader("⚠️ Missing Data Overview")
    st.write(data.isnull().sum())

    # Choose analysis
    analysis_type = st.sidebar.selectbox(
        "Choose Analysis Type",
        [
            "Sales by Store Location",
            "Most Popular Products",
            "Organic Coffee Analysis",
            "Eco_Friendly_cup Analysis",
            "Price vs Quantity (Line Plot)",  # Changed from Scatter Plot to Line Plot
            "Price Distribution (Histogram)"
        ]
    )

    # 1. Sales by Store Location
    if analysis_type == "Sales by Store Location":
        if 'Store_location' in data.columns:
            store_counts = data['Store_location'].value_counts()
            st.subheader("🏬 Sales by Store Location")
            st.bar_chart(store_counts)
        else:
            st.error("❌ 'Store_location' column is missing in the uploaded file.")

    # 2. Most Popular Products
    elif analysis_type == "Most Popular Products":
        if 'Product_type' in data.columns:
            top_products = data['Product_type'].value_counts().head(5)
            st.subheader("🏆 Top 5 Most Popular Products")
            st.bar_chart(top_products)
        else:
            st.error("❌ 'Product_type' column is missing in the uploaded file.")

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
            st.error("❌ 'Organic Coffee' column is missing in the uploaded file.")

    # 4. Eco_Friendly_cup Analysis
    elif analysis_type == "Eco_Friendly_cup Analysis":
        if 'Eco_Friendly_cup' in data.columns:
            eco_counts = data['Eco_Friendly_cup'].value_counts()
            fig = px.pie(
                names=eco_counts.index,
                values=eco_counts.values,
                title="♻️ Eco_Friendly_cup Usage"
            )
            st.plotly_chart(fig)
        else:
            st.error("❌ 'Eco_Friendly_cup' column is missing in the uploaded file.")
    
    # 5. Price vs Quantity (Line Plot)
    if analysis_type == "Price vs Quantity (Line Plot)":
        if 'Unit_price' in data.columns and 'Transaction_qty' in data.columns:
            st.subheader("📈 Price vs Quantity Line Plot")

            # Group by unit price and calculate the mean quantity for each price
            grouped_data = data.groupby('Unit_price')['Transaction_qty'].mean().reset_index()
            # Sort by unit price for a proper line plot
            grouped_data = grouped_data.sort_values('Unit_price')

            fig, ax = plt.subplots(figsize=(10, 6))
            # Create line plot
            ax.plot(grouped_data['Unit_price'], grouped_data['Transaction_qty'],
                    marker='o', linestyle='-', color='green', linewidth=2)

            ax.set_xlabel("Unit Price")
            ax.set_ylabel("Average Transaction Quantity")
            ax.set_title("Unit Price vs Quantity Sold")
            st.pyplot(fig)

# 🔍 Brief Analysis
            st.markdown("### 🔍 Brief Analysis")
            st.markdown("""
The line plot shows the relationship between Unit Price and Average Transaction Quantity.

- In the lower price range (around 2.0 to 2.5), the quantity sold fluctuates.
- A significant drop is observed near 2.6, followed by a rise reaching a peak around 4.0.
- After this peak, there's a noticeable decline in quantity sold as the price increases further.
""")
        else:
            st.error("❌ 'Unit_price' and/or 'Transaction_qty' columns are missing in the uploaded file.")

    # 6. Histogram: Price Distribution
    elif analysis_type == "Price Distribution (Histogram)":
        if 'Unit_price' in data.columns:
            st.subheader("📊 Price Distribution Histogram")
            fig, ax = plt.subplots()
            ax.hist(data['Unit_price'], bins=20, color='skyblue', edgecolor='black')
            ax.set_xlabel("Unit Price")
            ax.set_ylabel("Frequency")
            ax.set_title("Distribution of Unit Prices")
            st.pyplot(fig)
        else:
            st.error("❌ 'Unit_price' column is missing in the uploaded file.")

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
            st.error("❌ Columns 'Transaction_qty', 'Unit_price', or 'Product_type' are missing in the uploaded file.")
else:
    st.info("📂 Please upload a data file to begin analysis.")