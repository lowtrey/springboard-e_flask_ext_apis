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

# Mock POST Request
# more_data = {
#   "username": "chickenx",
#   "tweets": [
#     "hello!", "goodbye!", "bock bock!", {
#       "id": 1, "text": "my first tweet!"
#     }
#   ]
# }

# requests.post("https://en27bnye2btkl.x.pipedream.net", json=data)