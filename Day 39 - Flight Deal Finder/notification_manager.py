from flight_data import FlightData
from twilio.rest import Client
import os
import smtplib

# Email
MY_EMAIL = "hubert.smtp.test@gmail.com"
PASSWORD = "gcttfrotdomgzvev"

# SMS
account_sid = "AC9e87129e24b9cb746aa2527455a2538e"
auth_token = os.environ.get("SMS_AUTH_TOKEN")

#This class is responsible for sending notifications with the deal flight details.
class NotificationManager(FlightData):

    def __init__(self, flight_data):
        super().__init__(flight_data=flight_data)
        self.message = f"Low price alert! Only £{self.price} to fly from {self.city_from}-{self.iata_from} to " \
                       f"{self.city_to}-{self.iata_to}, from {self.departure_date} to {self.return_date}"

    def send_email(self):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:FLIGHT ALERT! £{self.price} from {self.city_from}-{self.iata_from} to "
                    f"{self.city_to}-{self.iata_to} \n\n{self.message}".encode('utf-8')
            )

    def send_sms(self):
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=self.message,
            from_="+19298225941",
            to="+44796188778"
        )

