import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
dataset = pd.read_csv('sales_data.csv')

# Calculate total revenue for each product
product_revenue = dataset.groupby('product_id')['revenue'].sum()

# Sort products by revenue in descending order
top_products = product_revenue.sort_values(ascending=False).head(10)

# Create a bar plot for top 10 products by revenue
plt.figure(figsize=(10, 6))
top_products.plot(kind='bar')
plt.title('Top 10 Products by Revenue')
plt.xlabel('Product ID')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()