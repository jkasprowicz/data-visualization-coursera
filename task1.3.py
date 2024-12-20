import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('/Users/joaokasprowicz/Desktop/historical_automobile_sales.csv')

print(df.head())

# Filter data for recession and non-recession periods
recession_data = df[df['Recession'] == 1]
non_recession_data = df[df['Recession'] == 0]

# Seaborn lineplot for comparison
plt.figure(figsize=(12, 6))
sns.lineplot(data=recession_data, x="Year", y="Automobile_Sales", hue="Vehicle_Type", marker="o")
sns.lineplot(data=non_recession_data, x="Year", y="Automobile_Sales", hue="Vehicle_Type", linestyle='--')
plt.title("Sales Trends During Recession and Non-Recession Periods")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.legend(title="Vehicle Type and Period")
plt.show()
