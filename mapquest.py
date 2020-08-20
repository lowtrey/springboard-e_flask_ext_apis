import requests
from secrets import API_KEY

response = requests.get(
  "http://www.mapquestapi.com/geocoding/v1/address",
  params={"key": API_KEY, "location": "712 Silver Street"}
)