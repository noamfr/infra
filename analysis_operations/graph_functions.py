import numpy as np
import pandas as pd
import os
import seaborn as sns
from matplotlib import pyplot as plt, use
from typing import List

plt.style.use('seaborn-darkgrid')
use('SVG')


def histogram(path: str,
              vector: np.ndarray,
              label: str,
              x_label: str,
              y_label: str,
              bins: int or None = None,
              x_ticks=None,
              add_mean_line: bool = False):

    plt.clf()
    plt.hist(vector, label=label, color='royalblue', bins=bins)
    plt.title(label=f'{label}_histogram', weight='bold')
    plt.xlabel(x_label, weight='bold')
    plt.ylabel(y_label, weight='bold')
    plt.xticks(ticks=x_ticks)
    plt.grid(True, alpha=0.8)

    if add_mean_line:
        mean = vector.mean()
        plt.axvline(mean, color='orange', linestyle='dashed', linewidth=1.5, label=f'mean: {round(mean, 1)}')

    plt.legend(loc='best', shadow=True)
    plt.tight_layout()
    plt.savefig(os.path.join(path, f'{label}_histogram.png'), dpi=500)


def bar_chart(x, height, title: str, x_label: str, y_label: str, path: str):
    plt.clf()
    plt.bar(x=x, height=height, color='royalblue')
    plt.title(title, weight='bold')
    plt.xlabel(x_label, weight='bold')
    plt.ylabel(y_label, weight='bold')
    plt.xticks(rotation=45, ha='right', fontsize=8)
    plt.ylim(0, round(max(height) * 1.3, 1))
    plt.grid(True, axis='y', linewidth=0.5, alpha=0.7)
    plt.tight_layout()
    plt.savefig(os.path.join(path, f'{title}_bar_chart.png'), dpi=500)


def lines_chart(data: pd.DataFrame, x: str, y: str, hue=None, style=None):
    plt.figure(figsize=(25, 12))
    sns.lineplot(x=x, y=y, data=data, hue=hue, style=style, markers=True, legend='full')
    plt.legend(fontsize=18, shadow=True)
    plt.xticks(np.arange(0, data[x].nunique(), 1), fontsize=16, fontweight='bold')
    plt.yticks(fontsize=14, fontweight='bold')
    plt.xlabel(x, fontsize=18, fontweight='bold')
    plt.ylabel(y, fontsize=18, fontweight='bold')
    plt.title(f'{hue} by {y}', fontsize=24, fontweight='bold')
    plt.show()


def correlation_matrix(
        corr: pd.DataFrame,
        labels: List[str],
        title: str,
        output_path: str,
        square: bool = False):

    use('tkagg')
    plt.clf()
    sns.heatmap(round(corr, 2), annot=True, vmin=-1, vmax=1, linewidth=0.5, cmap='RdBu',
                square=square, xticklabels=labels, yticklabels=labels)
    plt.xticks(fontsize=8, fontweight='bold', ha='right', rotation=45)
    plt.yticks(fontsize=8, fontweight='bold', va="center")
    plt.title(title, fontsize=10, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, f'{title}.png'))


def distribution_analysis(data: pd.DataFrame, feature_name: str, label: str):
    vec = data[feature_name]
    mini = vec.min()
    maxi = vec.max()
    rng = maxi - mini
    mean = vec.mean()
    median = vec.median()
    mode = vec.mode()[0]
    std = vec.std()
    skew = vec.skew()
    kurt = vec.kurtosis()
    points = mean - std, mean + std
    n = len(vec)

    plt.clf()
    plt.figure(figsize=(12, 6))
    sns.distplot(vec, hist=True, kde=True)
    sns.lineplot(points, [0, 0], color='black', label=f'std_dev: {round(std,2)}')
    sns.scatterplot([mini, maxi], [0, 0], color='orange', label=f"min/max{mini, maxi}", s=100, alpha=1)
    sns.scatterplot([mean], [0], color='red', label=f'mean: {round(mean,2)}', s=100, alpha=1)
    sns.scatterplot([median], [0], color='blue', label=f'median: {round(median, 2)}', s=100, alpha=1)
    sns.scatterplot([mode], [0], color='green', label=f'mode: {mode}', s=100, alpha=1)

    plt.xlabel(f'{feature_name}', fontsize=16)
    plt.ylabel('density', fontsize=16)
    plt.title(f'Distribution of {feature_name} for {label.upper()} (n={n})\nskew = {round(skew, 2)}; kurtosis = {round(kurt, 2)}', fontsize=18)
    plt.legend(fontsize=14, shadow=True, frameon=True)
    plt.tight_layout()
    plt.show()

