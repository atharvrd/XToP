import pandas as pd

def read_excel(file_path):

    sheets = pd.read_excel(
        file_path,
        sheet_name=None
    )

    return sheets