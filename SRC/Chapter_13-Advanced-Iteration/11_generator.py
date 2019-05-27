import requests
import time

urls = ("https://www.oreilly.com/", "https://twitter.com/", "https://www.google.com/")

for resp in [requests.get(url) for url in urls]:
    print(len(resp.content), "->", resp.status_code, "->", resp.url)

print("Printed using list")

time.sleep(5)
print("Printing using generator")

for resp in (requests.get(url) for url in urls):
    print(len(resp.content), "->", resp.status_code, "->", resp.url)
