import urllib.request

web_url = urllib.request.urlopen("https://www.example.com")

print("Result code:",  web_url.getcode())

data = web_url.read()
print(data)