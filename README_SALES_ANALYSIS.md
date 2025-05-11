kinda-alraiss
📊 Sales Analysis App
Welcome to the Sales Analysis App! This application provides insightful visualizations and analytics for your sales data. Simply upload your data file (Excel or CSV), and explore various analysis types to understand your sales performance better.

🛠 Features
Data Upload and Preview: Upload .xlsx or .csv files to start analyzing your sales data. Displays a preview of the uploaded data.
Missing Data Overview: Check for missing data and understand what columns might need attention.
Interactive Analysis Options:
Sales by Store Location: Visualize the distribution of sales across different store locations using bar charts.
Most Popular Products: Identify the top 5 most popular products.
Organic Coffee Analysis: Understand the distribution of organic coffee sales using pie charts.
Eco-Friendly Cup Analysis: Analyze the usage of eco-friendly cups with pie charts.
Price vs Quantity (Line Plot): Explore the relationship between unit prices and transaction quantities.
Price Distribution (Histogram): Visualize the distribution of unit prices with a histogram.
Revenue Calculation: Calculate and visualize revenue by product type.
🚀 How to Run the App
Install the required Python libraries:
Bash

pip install pandas streamlit plotly matplotlib
Save the logo1.png file in the correct path on your machine or update the st.image() path to match your logo location.

Run the app:

Bash

streamlit run app.py
📂 Input Data Requirements
The app supports .xlsx and .csv file formats.
Required columns for full functionality:
Store_location (for Sales by Store Location)
Product_type (for Most Popular Products and Revenue Calculation)
Organic Coffee (for Organic Coffee Analysis)
Eco_Friendly_cup (for Eco-Friendly Cup Analysis)
Unit_price and Transaction_qty (for Price vs Quantity and Revenue Calculation)
📈 Visualizations Available
1. Sales by Store Location
Bar Chart showing the distribution of sales by store location.
2. Most Popular Products
Bar Chart displaying the top 5 most popular products.
3. Organic Coffee Analysis
Pie Chart for the distribution of organic coffee sales.
4. Eco-Friendly Cup Analysis
Pie Chart for the usage of eco-friendly cups.
5. Price vs Quantity (Line Plot)
Line Plot showing the relationship between unit prices and average transaction quantities.
Includes an analysis of trends in pricing and sales volumes.
6. Price Distribution (Histogram)
Histogram visualizing the distribution of unit prices.
7. Revenue Calculation
Bar Chart summarizing revenue by product type.
🖼 Logo
The app includes a customizable logo, displayed at the top of the interface. Update the path in the code to match the location of your logo file.

⚙️ Example Screenshot
Example Screenshot

📌 Notes
Ensure your data file is clean and includes all required columns for the desired analysis.
If specific columns are missing, the app will display an error message for the respective analysis feature.
Customize the app further by adding new analysis types or visualizations as needed.
🧰 Dependencies
Python 3.7+
Libraries:
pandas
streamlit
plotly
matplotlib
📝 License
This project is licensed under the MIT License. Feel free to use and customize the app for your needs.

🤝 Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to submit a pull request.

📧 Contact
For any questions or inquiries, feel free to reach out:

Name: Ghinwa Allaoui, Kinda Rayes, Riam Abbas
Email: allaouighinwa@gmail.com ,reyeskinda@gmail.com ,riam.abbas97@gmail.com
GitHub: Ghinwa1981, kinda-alraiss, Riam24
