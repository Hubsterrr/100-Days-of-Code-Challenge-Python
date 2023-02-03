import requests

KIWI_API = "Lrh_w371oR5aua2XAE55QT3TTDyRMlxr"
HEADERS = {'apikey': KIWI_API}
FLY_FROM = "LON"
CURRENCY = "GBP"
# This class is responsible for talking to the Flight Search API.
class FlightSearch:

    def __init__(self, dest_iata, dateFrom, dateTo, stay_length):
        self.parameters = {
            "fly_from": FLY_FROM,
            "fly_to": dest_iata,
            "dateFrom": dateFrom,
            "dateTo": dateTo,
            "nights_in_dst_from": stay_length,
            "nights_in_dst_to": stay_length,
            "max_stopovers": 0,
            "curr": CURRENCY
        }

    def search_flight(self):
        response = requests.get(url="https://api.tequila.kiwi.com/v2/search", headers=HEADERS, params=self.parameters)
        response.raise_for_status()
        raw_data = response.json()
        cheapest_flight = raw_data["data"][0]
        return cheapest_flight

