import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('averages.csv')

sns.set(style="whitegrid")


# Função para gerar gráficos com dados agrupados
def scatter_plot_grouped(x, y, xlabel, ylabel, title, filename, df, bins, bin_label):
    df[f'{x}_grouped'] = pd.cut(df[x], bins=bins, labels=bin_label)
    grouped = df.groupby(f'{x}_grouped')[y].mean().reset_index()

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=f'{x}_grouped', y=y, data=grouped)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(filename, format='png')  # Salva o gráfico como arquivo PNG
    plt.close()  # Fecha o gráfico para evitar sobreposição


# Funções específicas para as perguntas de pesquisa
def analyze_rq01(df):
    bins_stars = [0, 10000, 20000, 30000, 40000, 50000, 100000]
    bin_labels_stars = ['0-10k', '10k-20k', '20k-30k', '30k-40k', '40k-50k', '50k-100k']

    scatter_plot_grouped('stars', 'average_cbo', 'Stars Group', 'CBO', 'Popularity vs CBO (Grouped)',
                         'rq01_cbo_grouped.png', df, bins_stars, bin_labels_stars)
    scatter_plot_grouped('stars', 'average_dit', 'Stars Group', 'DIT', 'Popularity vs DIT (Grouped)',
                         'rq01_dit_grouped.png', df, bins_stars, bin_labels_stars)
    scatter_plot_grouped('stars', 'average_lcom', 'Stars Group', 'LCOM', 'Popularity vs LCOM (Grouped)',
                         'rq01_lcom_grouped.png', df, bins_stars, bin_labels_stars)


def analyze_rq02(df):
    bins_age = [0, 2, 4, 6, 8, 10, 15, 20]
    bin_labels_age = ['0-2y', '2-4y', '4-6y', '6-8y', '8-10y', '10-15y', '15-20y']

    scatter_plot_grouped('age', 'average_cbo', 'Maturity (Years)', 'CBO', 'Maturity vs CBO (Grouped)',
                         'rq02_cbo_grouped.png', df, bins_age, bin_labels_age)
    scatter_plot_grouped('age', 'average_dit', 'Maturity (Years)', 'DIT', 'Maturity vs DIT (Grouped)',
                         'rq02_dit_grouped.png', df, bins_age, bin_labels_age)
    scatter_plot_grouped('age', 'average_lcom', 'Maturity (Years)', 'LCOM', 'Maturity vs LCOM (Grouped)',
                         'rq02_lcom_grouped.png', df, bins_age, bin_labels_age)


def analyze_rq03(df):
    bins_releases = [0, 10, 20, 30, 50, 100, 200]
    bin_labels_releases = ['0-10', '10-20', '20-30', '30-50', '50-100', '100-200']

    scatter_plot_grouped('releases', 'average_cbo', 'Releases Group', 'CBO', 'Activity vs CBO (Grouped)',
                         'rq03_cbo_grouped.png', df, bins_releases, bin_labels_releases)
    scatter_plot_grouped('releases', 'average_dit', 'Releases Group', 'DIT', 'Activity vs DIT (Grouped)',
                         'rq03_dit_grouped.png', df, bins_releases, bin_labels_releases)
    scatter_plot_grouped('releases', 'average_lcom', 'Releases Group', 'LCOM', 'Activity vs LCOM (Grouped)',
                         'rq03_lcom_grouped.png', df, bins_releases, bin_labels_releases)


def analyze_rq04(df):
    bins_loc = [0, 5000, 10000, 20000, 50000, 100000, 200000]
    bin_labels_loc = ['0-5k LOC', '5k-10k LOC', '10k-20k LOC', '20k-50k LOC', '50k-100k LOC', '100k-200k LOC']

    scatter_plot_grouped('sum_loc', 'average_cbo', 'LOC Group', 'CBO', 'Size (LOC) vs CBO (Grouped)',
                         'rq04_cbo_grouped.png', df, bins_loc, bin_labels_loc)
    scatter_plot_grouped('sum_loc', 'average_dit', 'LOC Group', 'DIT', 'Size (LOC) vs DIT (Grouped)',
                         'rq04_dit_grouped.png', df, bins_loc, bin_labels_loc)
    scatter_plot_grouped('sum_loc', 'average_lcom', 'LOC Group', 'LCOM', 'Size (LOC) vs LCOM (Grouped)',
                         'rq04_lcom_grouped.png', df, bins_loc, bin_labels_loc)


# Função principal que executa a análise para todas as perguntas
def main():
    analyze_rq01(df)
    analyze_rq02(df)
    analyze_rq03(df)
    analyze_rq04(df)


if __name__ == "__main__":
    main()
