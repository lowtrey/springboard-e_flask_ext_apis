import requests

term = "J Cole"

response = requests.get(
  "https://itunes.apple.com/search",
  params={"term": term, "limit": 5}
  )

data = response.json()

for result in data["results"]:
  print(result["trackName"])
  print(result["collectionName"])