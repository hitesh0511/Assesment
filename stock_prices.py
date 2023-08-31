import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('stock_prices.csv')

# Convert the 'date' column to a datetime object
df['date'] = pd.to_datetime(df['date'])

# Sort the DataFrame by the 'date' column
df = df.sort_values('date')

# Calculate the rolling 30-day moving average
df['30_day_ma'] = df['closing_price'].rolling(window=30).mean()

# Plotting the time series data
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['closing_price'], label='Closing Price')
plt.plot(df['date'], df['30_day_ma'], label='30-Day Moving Average', color='red')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Stock Prices and 30-Day Moving Average')
plt.legend()
plt.grid(True)
plt.show()