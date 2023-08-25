from validate_url import validate_url

# --- We ask the user for the url that he wants to convert to mp3 ---

def url_user():
    url = input('Ingresa la URL del artículo: ')
    url = validate_url(url)
    return url