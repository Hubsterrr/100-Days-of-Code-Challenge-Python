import requests
from datetime import datetime
import smtplib


def send_email():
    my_email = "hubert.smtp.test@gmail.com"
    password = "gcttfrotdomgzvev"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="hubert.smtp.test@gmail.com",
            msg="Subject:ISS\n\nLook Up!"
        )


# Constants
MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude

# Variables
in_range = False
is_dark = True


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour = time_now.hour


def is_dark():
    if hour <= sunrise or hour >= sunset:
        return True


if is_iss_overhead() and is_dark():
    print("send")
    send_email()

