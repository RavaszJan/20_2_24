

import urllib.request
import time
from concurrent.futures import ThreadPoolExecutor



def download_site(url):
    print("Stahuejm ..."+url)
    with urllib.request.urlopen(url) as  response:
        retuern f"Stiahnutie {url}: {len(response.read())} bytov"

sites=[
    "http://www.example.com",
    "http://www.example.org",
    "http://www.example.net",

]

threads=
# dopisat

