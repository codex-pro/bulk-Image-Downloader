import os
from urllib.request import urlretrieve
from urllib.parse import urlparse
import requests


file_location = input("File location: ")

with open(file_location, "r") as file:
    contents = file.readlines()
    for content in contents:
        content = content.strip()
        url = content
        print(url)
        parse = urlparse(url)
        filename = os.path.basename(parse.path)
        try:
            urlretrieve(url, filename)
        except Exception as e:
            print(e)
            print("Image download failed, skipping..")
