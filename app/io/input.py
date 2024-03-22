
def input_text():
    text = input("Enter text: ")
    return text

def read_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"Error: {str(e)}"

import pandas as pd

def read_with_pandas(file_path):
    try:
        data = pd.read_txt(file_path)
        return data
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"Error: {str(e)}"