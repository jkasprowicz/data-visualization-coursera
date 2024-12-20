import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('/Users/joaokasprowicz/Desktop/historical_automobile_sales.csv')



# Filter GDP data for recession and non-recession periods
gdp_recession = df[df['Recession'] == 1].groupby('Year')['GDP'].mean()
gdp_non_recession = df[df['Recession'] == 0].groupby('Year')['GDP'].mean()

# Create subplots
fig, ax = plt.subplots(1, 2, figsize=(14, 6), sharey=True)
ax[0].plot(gdp_recession, marker='o')
ax[0].set_title("GDP During Recession")
ax[0].set_xlabel("Year")
ax[0].set_ylabel("GDP")

ax[1].plot(gdp_non_recession, marker='o', color='orange')
ax[1].set_title("GDP During Non-Recession")
ax[1].set_xlabel("Year")

plt.tight_layout()
plt.show()
