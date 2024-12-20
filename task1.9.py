import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv('/Users/joaokasprowicz/Desktop/historical_automobile_sales.csv')

print(df.head())

# Filter for recession data
recession_sales = df[df['Recession'] == 1]

# Line plot for unemployment rate and sales
plt.figure(figsize=(12, 6))
for vehicle_type in recession_sales['Vehicle_Type'].unique():
    vehicle_data = recession_sales[recession_sales['Vehicle_Type'] == vehicle_type]
    plt.plot(vehicle_data['Year'], vehicle_data['unemployment_rate'], label=f"{vehicle_type} - Unemployment")
    plt.plot(vehicle_data['Year'], vehicle_data['Automobile_Sales'], linestyle='--', label=f"{vehicle_type} - Sales")

plt.title("Unemployment Rate vs. Sales During Recession")
plt.xlabel("Year")
plt.ylabel("Values")
plt.legend()
plt.show()