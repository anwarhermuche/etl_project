import pandas as pd

import os
import glob
from typing import List

"""
Função para ler os arquivos xlsx de uma pasta data/input
e retornar uma lista de dataframes

args: input_path (str): caminho da pasta com os arquivos

return: list[pd.DataFrame]: lista de dataframes com os arquivos lidos
"""

def extract_from_excel(input_path: str) -> List[pd.DataFrame]:
    files = glob.glob(os.path.join(input_path, "*.xlsx"))
    return [pd.read_excel(file) for file in files]