import pandas as pd
import os
from typing import DefaultDict


class Data_Frame_Printer:
    def __init__(self, path: str):
        self.path = path

    def print_df_from_dict(self, default_dict: DefaultDict, file_name: str):
        df = pd.DataFrame(default_dict)
        df.to_csv(os.path.join(self.path, file_name))
