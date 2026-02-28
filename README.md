# Sales-Data-Analysis-Python-SQLite-Power-BI


🚀 Overview
This project simulates a real-world workflow performed by a Junior Data Analyst, covering the complete ETL process (Extract, Transform, Load) and the development of an interactive Business Intelligence Dashboard.
The main objective was to transform raw sales data into a clean, structured and reliable analytical base, enabling strategic decision-making through data visualization.

🏗️ Project Architecture

CSV File → Python (ETL) → SQLite Database → Power BI Dashboard
The project follows a structured data pipeline:
Data extraction from CSV files
Data cleaning and validation using Python
Storage in a relational SQLite database
Business analysis through Power BI

🐍 Data Engineering – Python (ETL)
The ETL process was developed using Pandas, applying best practices in data preparation.
Extract
Reading sales data from CSV
Validating structure and columns
Transform
Converting date columns to proper datetime format
Cleaning monetary values
Removing inconsistent or invalid records
Handling missing values
Creating calculated metrics such as total revenue
Load
Storing the processed data into a SQLite database
Ensuring structured data ready for analysis
This process guarantees that the dataset is clean, organized and reliable before analysis.

🗄️ Database – SQLite
After transformation, the data was stored in SQLite, enabling structured queries and business analysis such as:
Revenue per customer
Purchase frequency
Average ticket
Revenue distribution by city
Product performance
The separation of responsibilities ensures:
Python → Data Engineering
SQL → Analytical Queries

📊 Business Intelligence – Power BI Dashboard
An interactive dashboard was developed to provide strategic insights and support decision-making.

📈 Monthly Revenue Evolution
Identifies growth trends and seasonality patterns.

💰 Key Performance Indicators (KPIs)
Total Revenue
Total Sales
Total Items Sold
Average Ticket

🏆 Top Selling Product
Highlights the product with the highest sales volume.

🌎 Revenue by City
Shows geographical concentration of performance.

📦 Product Mix Analysis
Displays distribution of sales volume across products.
Each visualization was designed to answer a specific business question, focusing on clarity and decision-making impact rather than visual complexity.

🎯 Business Questions Answered
Which product generates the highest revenue?
Is the most sold product also the most profitable?
Which city concentrates the largest share of revenue?
Is revenue growing consistently over time?
How diversified is the product portfolio?

📚 Skills Demonstrated
Data Cleaning and Validation
ETL Pipeline Development
Python (Pandas)
SQLite Integration
Data Modeling
DAX Measures
Business Intelligence Dashboard Design
Analytical Thinking

🛠️ Tools Used
Python
Pandas
SQLite
Power BI
DAX

▶️ How to Run the Project
Clone this repository
Install Python (3.10+)
Install required libraries (Pandas)
Run the ETL script to generate the SQLite database
Open the Power BI file (.pbix)
Refresh the data source connection if necessary

👨‍💻 Author
Renan

Technology student focused on Data & AI Engineering.
