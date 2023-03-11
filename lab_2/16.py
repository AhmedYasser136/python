def replace_keywords(string, **kwargs):
    for key, value in kwargs.items():
        string = string.replace(key, value)
    return string
