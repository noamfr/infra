import numpy as np
from typing import List


def build_nd_array_from_object_list(object_list: List, field_name: str, remove_missing_values: bool = False):

    vector = [getattr(obj, field_name) for obj in object_list]

    if remove_missing_values:
        idx_to_remove = [idx for idx, value in enumerate(vector) if value is None]

        good_values = []
        for idx in range(len(vector)):
            if idx not in idx_to_remove:
                good_values.append(vector[idx])

        vector = good_values
        vector = [float(value) for value in vector]

    vector = np.array(vector)

    return vector
