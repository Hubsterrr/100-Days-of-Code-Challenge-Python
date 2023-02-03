# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
import datetime as dt


STAY_LENGTH = 7


# Get today's date
today_raw = dt.datetime.now()
six_months_later_raw = today_raw + dt.timedelta(days=182)

# Format dates
today = today_raw.strftime("%d/%m/%Y")
six_months_later = six_months_later_raw.strftime("%d/%m/%Y")

# Get info from google sheet
data = DataManager()
flight_data = data.get_flight_data()

# Check each destination if there is a better deal
flight_deal_id = 2
for flight_from_sheet in flight_data:

    # Get the lowest price and iata code from Google sheet (if "lowest price" is empty put dummy value)
    try:
        lowest_price = flight_from_sheet['lowestPrice']
    except KeyError:
        lowest_price = 100000

    iata_code = flight_from_sheet["iataCode"]

    # Search the destination
    flight_data = FlightSearch(iata_code, today, six_months_later, STAY_LENGTH)
    cheapest_flight = flight_data.search_flight()
    cheapest_flight_data = FlightData(cheapest_flight)

    # If new deal is better than the one in Google sheet - send info and update deal
    if cheapest_flight_data.price < lowest_price:
        data.update_flight_deal(deal_id=flight_deal_id,
                                deal_price=cheapest_flight_data.price,
                                search_date=today,
                                departure_date=cheapest_flight_data.departure_date,
                                return_date=cheapest_flight_data.return_date)
        #Send Email

        #Send SMS via Twilio API

    flight_deal_id += 1
