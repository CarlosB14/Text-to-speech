import validators


# --- Validate if the URL is correct ---
def validate_url(url):
    validate = True
    while validate:
        if validators.url(url):
            print('Correct URL')
            validate = False
            return url
        else:
            print('Incorrect URL')
            url = input('Enter the URL of the article: Example: https://name.com/ ')