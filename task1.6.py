import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv('/Users/joaokasprowicz/Desktop/historical_automobile_sales.csv')
pd.set_option('display.max_columns', None)


# Filter data for recession periods
recession_data = df[df['Recession'] == 1]

# Scatter plot for Price vs. Sales during recession
plt.figure(figsize=(10, 6))
plt.scatter(recession_data['Price'], recession_data['Automobile_Sales'], alpha=0.6, color='blue')
plt.title("Price vs. Sales Volume During Recessions")
plt.xlabel("Average Price (USD)")
plt.ylabel("Automobile Sales")
plt.grid(True)
plt.show()