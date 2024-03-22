
def print_to_console(text):
    print(text)

def write_to_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        return "Content has been successfully written to the file."
    except Exception as e:
        return f"Error: {str(e)}"
