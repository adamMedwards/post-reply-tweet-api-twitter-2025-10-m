thondef load_cookie(file_path):
    """
    Load the Twitter login cookie from a file.
    """
    with open(file_path, "r") as file:
        cookie = file.read().strip()
    
    return cookie