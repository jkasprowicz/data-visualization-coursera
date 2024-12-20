import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/joaokasprowicz/Desktop/historical_automobile_sales.csv')

# Aggregate sales by year
yearly_sales = df.groupby('Year')['Automobile_Sales'].sum()

# Plot line chart
plt.figure(figsize=(10, 6))
yearly_sales.plot(kind='line', marker='o', title="Yearly Automobile Sales")
plt.xlabel("Year")
plt.ylabel("Automobile_Sales")
plt.grid(True)
plt.show()

