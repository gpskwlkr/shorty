def check(url):
    if url[:4] != 'http':
        url = f'http://{url}'

    return url