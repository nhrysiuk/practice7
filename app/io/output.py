
def print_to_console(text):
    """
    Prints text to the console.

    Args:
    text (str): The text to be printed.
    """
    print(text)

def write_to_file(text):
    """
    Writes content to a file using Python's built-in capabilities.

    Args:
    text (str): The text to be written to the file.
    """

    with open("file_for_output.txt", 'w') as file:
        file.write(text)

def write_pandas(data):
    """
    Writes content to a file using Pandas.

     Args:
    data (pandas.DataFrame): Input value that will be written to file.
    """
    data.to_csv("file_for_output.csv")