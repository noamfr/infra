import os
import pandas as pd
from typing import Dict, List


def save_df_as_table(df: pd.DataFrame, column_order: List[str],  path: str, file_name: str):
    df = df[column_order]
    df.to_csv(os.path.join(path, file_name))
