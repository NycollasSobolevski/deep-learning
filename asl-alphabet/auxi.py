import os

def countImages(path):
    length = 0
    content = os.listdir(path)
    for clases in content:
        items = os.listdir(f'{path}/{clases}')
        length += len(items)
    return length