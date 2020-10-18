import numpy as np
import os
from matplotlib import pyplot as plt

plt.style.use('seaborn-darkgrid')


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
    plt.title(label=f'{label}_histogram')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(ticks=x_ticks)
    plt.grid(True, alpha=0.8)

    if add_mean_line:
        mean = vector.mean()
        plt.axvline(mean, color='orange', linestyle='dashed', linewidth=1.5, label=f'mean: {round(mean, 1)}')

    plt.legend(loc='best', shadow=True)
    plt.tight_layout()
    plt.savefig(os.path.join(path, f'{label}_histogram.png'))


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
