import numpy as np


def remove_missing_values_from_vector(vector):
    idx_to_remove = []
    for idx in range(len(vector)):
        if vector[idx] in [None, np.nan]:
            idx_to_remove.append(idx)

    vector = [value for idx, value in enumerate(vector) if idx not in idx_to_remove]
    return vector
