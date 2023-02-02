# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
import datetime as dt

#Get today's date
today_raw = dt.datetime.now()
six_months_later_raw = today_raw + dt.timedelta(days=182)
today = today_raw.strftime("%d/%m/%Y")
six_months_later = six_months_later_raw.strftime("%d/%m/%Y")

data = DataManager()
flight_data = data.get_flight_data()
iata_list = data.get_iata_codes()

for flight_from_sheet in flight_data:
    lowest_price = flight_from_sheet['lowestPrice']
    iata_code = flight_from_sheet["iataCode"]

    flight_data = FlightSearch(iata_code, today, six_months_later)
    cheapest_flight = flight_data.search_flight()
    cheapest_flight_data = FlightData(cheapest_flight)

    
    if cheapest_flight_data.price < lowest_price:
        pass
    #Twillio

#TO DO:
# - IF CHEAPER - SEND SMS NOTIFICATION ABOUT DESTINATION WITH DATE AND PRICE
