# boot
import urllib.request
import time

def download_site(url):
    with urllib.request.urlopen(url) as response:
        print(f"Stiahnutie {url}: {len(response.read())} bytov")


sites= [
    "http://www.example.com",
    "http://www.example.org",
    "http://www.example.net",
    "http://www.apple.com",
    "http://www.hbo.sk",
    "http://www.netflix.com",
]
start_time=time.time()
for site in sites:
    download_site(site)

duration= time.time() - start_time
print(f"stiahnute {len(sites)} stranok za {duration} sekund")
