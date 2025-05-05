import urllib.request
import json

# Open the URL and read the data
web_url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
response = urllib.request.urlopen(web_url)

print("Result code:", response.getcode())

data = response.read()
# print(data)
json_data = json.loads(data)
print(json_data["text"])