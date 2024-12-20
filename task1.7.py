import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv('/Users/joaokasprowicz/Desktop/historical_automobile_sales.csv')


recession_ad_exp = df[df['Recession'] == 1].groupby('Vehicle_Type')['Advertising_Expenditure'].sum()

# Plot pie chart
recession_ad_exp.plot(kind='pie', autopct='%1.1f%%', title="Ad Expenditure by Vehicle Type During Recession")
plt.ylabel("")
plt.show()