import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.iata_list = []


    def get_flight_data(self):
        response = requests.get(url="https://api.sheety.co/e3c04c44689f6e1dbab65cb8ab4e1ac1/flightDeals/prices")
        response.raise_for_status()
        data = response.json()["prices"]
        return data

    def update_flight_deal(self, deal_id, deal_price, search_date, departure_date, return_date):
        deal_data = {
            "price": {
                "lowestPrice": deal_price,
                "dateWhenFound": search_date,
                "departureDateLondon": departure_date,
                "returnDate": return_date,
            }
        }
        response = requests.put(url=f"https://api.sheety.co/e3c04c44689f6e1dbab65cb8ab4e1ac1/flightDeals/prices/{deal_id}",
                                json=deal_data)
        response.raise_for_status()
