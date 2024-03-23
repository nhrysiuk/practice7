
def input_text():
    """
    Prompts the user to input text from the console.

    Returns:
    str: The text entered by the user.
    """
    text = input("Enter text: ")
    return text

def read_from_file(file_path):
    """
    Reads content from a file.

    Args:
    file_path (str): The path to the file.

    Returns:
    str: The content of the file.
    """
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
    """
    Reads data from a file using pandas.

    Args:
    file_path (str): The path to the file.

    Returns:
    DataFrame: The data read from the file.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"Error: {str(e)}"