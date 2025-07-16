from typing import List

import pandas as pd

"""
Função para transformar uma lista de dataframes em um único dataframe

args: dataframes (List[pd.DataFrame]): lista de dataframes a serem transformados

return: pd.DataFrame: dataframe transformado    
"""


def concat_dataframes(dataframes: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(dataframes, ignore_index=True)
