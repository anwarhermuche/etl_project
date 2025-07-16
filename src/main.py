import os
from dotenv import load_dotenv

from pipeline.extract import extract_from_excel

load_dotenv()

if __name__ == "__main__":
    input_file_path = os.environ.get("INPUT_FILE_PATH")
    if input_file_path is None:
        raise ValueError("INPUT_FILE_PATH is not set")

    files = extract_from_excel(input_file_path)
    print(files)
