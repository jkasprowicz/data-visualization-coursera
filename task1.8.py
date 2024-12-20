import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv('/Users/joaokasprowicz/Desktop/historical_automobile_sales.csv')

ad_exp = df.groupby('Recession')['Advertising_Expenditure'].sum()

# Plot pie chart
ad_exp.plot(kind='pie', autopct='%1.1f%%', labels=['Non-Recession', 'Recession'], title="Advertising Expenditure")
plt.ylabel("")  # Removes default ylabel
plt.show()