thonimport json

def export_to_file(data, file_path):
    """
    Export the structured tweet data to a file.
    """
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)