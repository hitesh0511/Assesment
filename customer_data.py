import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('customer_data.csv')

# Remove duplicates based on 'customer_id'
df = df.drop_duplicates(subset='customer_id')

# Handle missing values (replace NaN values in 'purchases' with 0)
df['purchases'].fillna(0, inplace=True)

# Calculate the average number of purchases for each gender
average_purchases_by_gender = df.groupby('gender')['purchases'].mean()

# Print the results
print(average_purchases_by_gender)