def valid_form(username: str, password: str):
    if not username or not password or len(password)<5:
        return False

    return True