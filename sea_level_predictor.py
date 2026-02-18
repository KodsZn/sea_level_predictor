import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1️⃣ Read data
    df = pd.read_csv("epa-sea-level.csv")
    print(df.columns)

    # 2️⃣ Scatter plot (النقاط الأصلية)
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # ==============================
    # 3️⃣ First line of best fit (1880 → 2050)
    # ==============================
    result = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create years until 2050
    years_extended = pd.Series(range(1880, 2051))
    sea_level_predicted = result.slope * years_extended + result.intercept

    plt.plot(years_extended, sea_level_predicted, 'r')

    # ==============================
    # 4️⃣ Second line (2000 → 2050)
    # ==============================
    df_2000 = df[df["Year"] >= 2000]

    result_recent = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])

    years_recent = pd.Series(range(2000, 2051))
    sea_level_recent = result_recent.slope * years_recent + result_recent.intercept

    plt.plot(years_recent, sea_level_recent, 'green')

    # ==============================
    # 5️⃣ Labels & title
    # ==============================
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    plt.savefig("sea_level_plot.png")
    return plt.gca()

draw_plot()
plt.show()
