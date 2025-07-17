import os
from dotenv import load_dotenv

from src.pipeline.extract import extract_from_excel
from src.pipeline.transform import concat_dataframes
from src.pipeline.load import load_to_excel

load_dotenv()


def main():
    input_file_path = os.environ.get("INPUT_FILE_PATH")
    output_file_path = os.environ.get("OUTPUT_FILE")

    if input_file_path is None:
        raise ValueError("INPUT_FILE_PATH is not set")
    if output_file_path is None:
        raise ValueError("OUTPUT_FILE is not set")

    files = extract_from_excel(input_file_path)
    dataframe = concat_dataframes(files)
    load_to_excel(dataframe, output_file_path)


if __name__ == "__main__":
    main()
