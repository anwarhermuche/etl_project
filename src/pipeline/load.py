import pandas as pd

""""
Transforma um dataframe em um arquivo xlsx

args: dataframe (pd.DataFrame): dataframe a ser transformado

return: None
"""


def load_to_excel(dataframe: pd.DataFrame, output_path: str) -> None:
    dataframe.to_excel(output_path, index=False)


if __name__ == "__main__":
    load_to_excel(
        pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]}), "data/output/output.xlsx"
    )
