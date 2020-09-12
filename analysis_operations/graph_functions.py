import numpy as np
import os
from matplotlib import pyplot as plt


def hist(path: str,
         vector: np.ndarray,
         label: str,
         x_label: str,
         y_label: str,
         add_mean_line: bool = False):

    plt.clf()
    plt.hist(vector, label=label, color='royalblue')
    plt.title(label=f'{label}_histogram')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)

    if add_mean_line:
        mean = vector.mean()
        plt.axvline(mean, color='orange', linestyle='dashed', linewidth=1.5, label=f'mean: {round(mean, 1)}')

    plt.legend(loc='best', shadow=True)
    plt.tight_layout()
    plt.savefig(os.path.join(path, f'{label}_histogram.png'))
