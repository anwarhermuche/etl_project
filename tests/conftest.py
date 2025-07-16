import pytest
import pandas as pd


@pytest.fixture
def dataframes():
    arrange = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    arrange_2 = pd.DataFrame({"col1": [7, 8, 9], "col2": [10, 11, 12]})
    arrange_3 = pd.DataFrame({"col1": [13, 14, 15], "col2": [16, 17, 18]})
    return [arrange, arrange_2, arrange_3]
