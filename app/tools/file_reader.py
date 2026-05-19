def read_text_file(file_path):

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    except Exception as e:
        return f"Error reading file: {e}"