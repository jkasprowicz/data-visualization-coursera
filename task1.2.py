import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/joaokasprowicz/Desktop/historical_automobile_sales.csv')


vehicle_sales = df.groupby(['Year', 'Vehicle_Type'])['Automobile_Sales'].sum().unstack()

# Plot sales trends for each vehicle type
vehicle_sales.plot(kind='line', figsize=(12, 8), title="Sales Trends by Vehicle Type")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.legend(title="Vehicle Type")
plt.grid(True)
plt.show()