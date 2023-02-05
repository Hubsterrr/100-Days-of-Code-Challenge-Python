import requests

KIWI_API = "Lrh_w371oR5aua2XAE55QT3TTDyRMlxr"
HEADERS = {'apikey': KIWI_API}

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.update_iata_codes()


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

    # NOT FINISHED (Ran out of calls in sheety api)
    def update_iata_codes(self):
        data = self.get_flight_data()
        for destination in data:
            city = destination["city"]
            print(city)
            parameters = {
                "term": city,
                "locale": "en_US",
                "location_types": city,
            }

            response = requests.get(url="https://api.tequila.kiwi.com/locations/query", headers=HEADERS, params=parameters)
            response.raise_for_status()
            raw_data = response.json()
            iata_code = raw_data["locations"][0]["city"]["code"]
            print(iata_code)

