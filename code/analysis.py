import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../averages.csv')

sns.set(style="whitegrid")

def scatter_plot(x, y, xlabel, ylabel, title, filename, df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=x, y=y, data=df)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(filename, format='png')  # Save plot as a PNG file
    plt.close()  # Close the plot to avoid overlap

def analyze_rq01(df):
    scatter_plot('stars', 'average_cbo', 'Stars', 'CBO', 'Popularity vs CBO', '../rq01_cbo.png', df)
    scatter_plot('stars', 'average_dit', 'Stars', 'DIT', 'Popularity vs DIT', '../rq01_dit.png', df)
    scatter_plot('stars', 'average_lcom', 'Stars', 'LCOM', 'Popularity vs LCOM', '../rq01_lcom.png', df)

def analyze_rq02(df):
    scatter_plot('age', 'average_cbo', 'Maturity (Years)', 'CBO', 'Maturity vs CBO', '../rq02_cbo.png', df)
    scatter_plot('age', 'average_dit', 'Maturity (Years)', 'DIT', 'Maturity vs DIT', '../rq02_dit.png', df)
    scatter_plot('age', 'average_lcom', 'Maturity (Years)', 'LCOM', 'Maturity vs LCOM', '../rq02_lcom.png', df)

def analyze_rq03(df):
    scatter_plot('releases', 'average_cbo', 'Releases', 'CBO', 'Activity vs CBO', '../rq03_cbo.png', df)
    scatter_plot('releases', 'average_dit', 'Releases', 'DIT', 'Activity vs DIT', '../rq03_dit.png', df)
    scatter_plot('releases', 'average_lcom', 'Releases', 'LCOM', 'Activity vs LCOM', '../rq03_lcom.png', df)

def analyze_rq04(df):
    scatter_plot('sum_loc', 'average_cbo', 'LOC', 'CBO', 'Size (LOC) vs CBO', '../rq04_cbo.png', df)
    scatter_plot('sum_loc', 'average_dit', 'LOC', 'DIT', 'Size (LOC) vs DIT', '../rq04_dit.png', df)
    scatter_plot('sum_loc', 'average_lcom', 'LOC', 'LCOM', 'Size (LOC) vs LCOM', '../rq04_lcom.png', df)

def main():
    analyze_rq01(df)
    analyze_rq02(df)
    analyze_rq03(df)
    analyze_rq04(df)


if __name__ == "__main__":
    main()

