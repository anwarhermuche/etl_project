import pandas as pd
from src.pipeline.transform import concat_dataframes


def test_concat_dataframes(dataframes):

    result = concat_dataframes(dataframes)

    assert result.equals(pd.concat(dataframes, ignore_index=True)), "Os dataframes não são iguais"