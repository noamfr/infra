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


def distribution_analysis(
        output_path: str,
        data: pd.DataFrame,
        feature_name: str):

    vec = data[feature_name]
    mini = vec.min()
    maxi = vec.max()
    rng = maxi - mini
    mean = vec.mean()
    median = vec.median()
    std = vec.std()
    skew = vec.skew()
    kurt = vec.kurtosis()
    points = mean - std, mean + std

    sns.distplot(vec, hist=True, kde=True)
    sns.lineplot(points, [0, 0], color='black', label="std_dev")
    sns.scatterplot([mini, maxi], [0, 0], color='orange', label="min/max")
    sns.scatterplot([mean], [0], color='red', label="mean")
    sns.scatterplot([median], [0], color='blue', label="median")

    plt.xlabel(f'{feature_name}', fontsize=20)
    plt.ylabel('density')
    plt.title(f'std_dev = {round(std, 2)}; kurtosis = {round(kurt,2)};\nskew = {round(skew, 2)};range = {round(rng, 2)}\nmean = {round(mean, 2)}; median = {round(median, 2)}')
    plt.savefig(os.path.join(output_path, f'{feature_name}_distribution.png'))




