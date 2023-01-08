import requests
import os
from twilio.rest import Client

api_key = os.environ.get("OWM_API_KEY")
account_sid = "AC9e87129e24b9cb746aa2527455a2538e"
auth_token = os.environ.get("SMS_AUTH_TOKEN")

parameters = {
    "lat": 51.5085,
    "lon": -0.1257,
    "appid": api_key,
}

response = requests.get(url="http://api.openweathermap.org/data/2.5/forecast?", params=parameters)
response.raise_for_status()
data = response.json()

hour_list = data["list"]
will_rain = False

for hour in hour_list[:8]:
    weather_id = hour["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️ with you",
        from_="+19298225941",
        to="+44796188778"
    )
    print(message.status)

