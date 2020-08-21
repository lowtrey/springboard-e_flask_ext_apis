from flask import Flask, render_template, request
import requests
from secrets import API_KEY

API_BASE_URL = "http://www.mapquestapi.com/geocoding/v1"

app = Flask(__name__)

@app.route("/")
def show_address_form():
  return render_template("address_form.html")

@app.route("/geocode")
def get_location():
  address = request.args["address"]
  response = requests.get(
    f"{API_BASE_URL}/address", 
    params={"key": API_KEY, "location": address})

  data = response.json()
  lat = data["results"][0]["locations"][0]["latLng"]["lat"]
  lng = data["results"][0]["locations"][0]["latLng"]["lng"]
  coords = {"lat": lat, "lng": lng}
  return render_template("address_form.html", coords=coords)
