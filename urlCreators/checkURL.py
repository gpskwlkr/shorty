def check(url):
    if url[:8] != 'https://' or url[:7] != 'http://':
        url = f'http://{url}'

    return url