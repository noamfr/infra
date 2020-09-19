from typing import Dict
from collections import defaultdict
import numpy as np


class Descriptive_Table:
    def __init__(self, vector_dict: Dict[str, np.ndarray]):
        self.__vector_dict = vector_dict

    def get_descriptive_table(self):
        data_dict = defaultdict(list)

        for field in self.__vector_dict:
            vector = self.__vector_dict[field]

            count = len(vector)
            avg = vector.mean()
            std = vector.std()
            minimum = vector.min()
            q1 = np.quantile(vector, 0.25)
            median = np.quantile(vector, 0.50)
            q3 = np.quantile(vector, 0.75)
            maximum = vector.max()

            data_dict['field'].append(field)
            data_dict['count'].append(count)
            data_dict['mean'].append(round(avg, 2))
            data_dict['std'].append(round(std, 2))
            data_dict['min'].append(round(minimum, 2))
            data_dict['q1'].append(q1)
            data_dict['median'].append(round(median, 2))
            data_dict['q3'].append(q3)
            data_dict['max'].append(round(maximum, 2))

        return data_dict
