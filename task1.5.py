import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv('/Users/joaokasprowicz/Desktop/historical_automobile_sales.csv')

# Add a 'Season' column (optional, can be replaced by grouping by Month)
season_mapping = {
    "Jan": "Winter", "Feb": "Winter", "Mar": "Spring",
    "Apr": "Spring", "May": "Spring", "Jun": "Summer",
    "Jul": "Summer", "Aug": "Summer", "Sep": "Fall",
    "Oct": "Fall", "Nov": "Fall", "Dec": "Winter"
}
df['Season'] = df['Month'].map(season_mapping)

# Group by Month and calculate average sales
monthly_sales = df.groupby("Month")["Automobile_Sales"].mean().reset_index()
monthly_sales['Bubble Size'] = monthly_sales['Automobile_Sales'] / 10  # Adjust size for visualization

# Plot bubble plot
plt.figure(figsize=(12, 8))
scatter = sns.scatterplot(
    data=monthly_sales,
    x="Month",
    y="Automobile_Sales",
    size="Bubble Size",
    sizes=(50, 500),
    hue="Automobile_Sales",  # Optional: use color to indicate sales levels
    palette="coolwarm",
    alpha=0.7
)

# Add title and labels
plt.title("Impact of Seasonality on Automobile Sales", fontsize=16)
plt.xlabel("Month")
plt.ylabel("Automobile Sales")
plt.legend(title="Bubble Size (Scaled Sales)")
plt.grid(True)
plt.show()
