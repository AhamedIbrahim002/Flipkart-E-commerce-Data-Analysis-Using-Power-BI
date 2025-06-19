import pandas as pd

# Load the dataset
file_path = 'C:/Users/Administrator/Documents/bi/flipkart_com-ecommerce_sample.csv'
data = pd.read_csv(file_path)

# Drop unnecessary columns
data_cleaned = data.drop(columns=['uniq_id', 'crawl_timestamp', 'product_url', 'image', 'product_specifications'])

# Handle missing values: replace "No rating available" with a default value of 0 for ratings
data_cleaned['product_rating'].replace('No rating available', 0, inplace=True)
data_cleaned['overall_rating'].replace('No rating available', 0, inplace=True)

# Convert rating columns to numeric (if applicable) and prices to floats
data_cleaned['product_rating'] = pd.to_numeric(data_cleaned['product_rating'], errors='coerce').fillna(0)
data_cleaned['overall_rating'] = pd.to_numeric(data_cleaned['overall_rating'], errors='coerce').fillna(0)
data_cleaned['retail_price'] = pd.to_numeric(data_cleaned['retail_price'], errors='coerce').fillna(0)
data_cleaned['discounted_price'] = pd.to_numeric(data_cleaned['discounted_price'], errors='coerce').fillna(0)

# Drop duplicates if any
data_cleaned.drop_duplicates(subset=['product_name', 'brand', 'retail_price'], inplace=True)

# Handle missing values for other columns (if needed)
data_cleaned.fillna('Not available', inplace=True)

# Save the cleaned data to a new CSV file for Power BI
cleaned_file_path = 'C:/Users/Administrator/Documents/bi/flipkart_cleaned_for_powerbi.csv'
data_cleaned.to_csv(cleaned_file_path, index=False)

cleaned_file_path
