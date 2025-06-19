
📊 Flipkart E-commerce Data Analysis Using Power BI
====================================================

🎯 AIM:
-------
The goal of this project is to analyze product ratings, pricing, and brand performance on Flipkart using Power BI to derive actionable business insights.

📁 DATASET OVERVIEW:
---------------------
- Source: Flipkart E-commerce data from Kaggle
- Fields: Brand, Product Name, Discounted Price, Retail Price, Product Rating, Flipkart Advantage

🔧 DATA CLEANING (Python):
----------------------------
Performed using the script `cleaned.py`. Key steps:
1. Removed unnecessary columns:
   - 'uniq_id', 'crawl_timestamp', 'product_url', 'image', 'product_specifications'
2. Handled missing ratings by replacing "No rating available" with `0`
3. Converted columns to appropriate data types (numeric, float)
4. Removed duplicates using `product_name`, `brand`, and `retail_price`
5. Replaced remaining nulls with `'Not available'`
6. Saved cleaned dataset to:
   - `flipkart_cleaned_for_powerbi.csv`

📌 Script Summary:
-------------------
Example:
    data = pd.read_csv('flipkart_com-ecommerce_sample.csv')
    data_cleaned = data.drop(columns=[...])
    data_cleaned['product_rating'].replace('No rating available', 0, inplace=True)
    ...
    data_cleaned.to_csv('flipkart_cleaned_for_powerbi.csv', index=False)

🧮 DATA TRANSFORMATION:
-------------------------
Performed inside Power BI (DAX/Power Query):
- Created calculated columns and measures:
  - Total sales
  - Discount percentage
  - Average product rating

📊 ANALYSIS & VISUALIZATIONS:
------------------------------
1. Sales by Brand  
   → Bar chart showing total sales by brand (based on discounted price)

2. Product Rating by Name  
   → Shows which products are more highly rated by customers

3. Flipkart Advantage Analysis  
   → Pie chart showing % of products under Flipkart Advantage and their effect on sales

4. Retail vs Discounted Price Comparison  
   → Bar/line chart comparing pricing strategies across brands

🔍 KEY FINDINGS:
-----------------
- Brands like `@home`, `3D Mat`, and `Tarkan` dominate sales
- Flipkart Advantage products generally have better ratings
- "Florentyne" and "JD X Alloy" are among the highest-rated categories
- Deep discounts correlate with higher sales volumes

✅ CONCLUSION:
---------------
- Discount strategy significantly affects product performance
- Brand reputation and customer satisfaction are tied to higher ratings
- Flipkart Advantage appears to positively influence product perception and sales

📄 FILES INCLUDED:
-------------------
- flipkart_com-ecommerce_sample.csv → Raw dataset
- cleaned.py → Python script for cleaning
- flipkart_cleaned_for_powerbi.csv → Cleaned data used in Power BI
- Documentation.docx → Summary and explanation
- README.txt → You’re reading this!

📧 AUTHOR:
-----------
Name: Ahamed  
Email: ahamedibrahiminfo@gmail.com  

Feel free to fork, enhance, or reference this project for learning purposes.
