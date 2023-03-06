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

    def update_iata_codes(self):
        data = self.get_flight_data()
        dest_id = 2
        for destination in data:
            city = destination["city"]

            parameters = {
                "term": city,
                "locale": "en_US",
                "location_types": "city",
            }

            response = requests.get(url="https://api.tequila.kiwi.com/locations/query", headers=HEADERS, params=parameters)
            response.raise_for_status()
            raw_data = response.json()
            try:
                iata_code = raw_data["locations"][0]["code"]

                iata_data = {
                            "price": {"iataCode": iata_code}
                            }

                response = requests.put(url=f"https://api.sheety.co/e3c04c44689f6e1dbab65cb8ab4e1ac1/flightDeals/prices/{dest_id}",
                                    json=iata_data)
                response.raise_for_status()
            except IndexError:
                self.update_error(dest_id)
            dest_id += 1
    def update_error(self, flight_deal_id):
        error = {
            "price": {"lowestPrice": "ERROR"}
        }
        response = requests.put(
            url=f"https://api.sheety.co/e3c04c44689f6e1dbab65cb8ab4e1ac1/flightDeals/prices/{flight_deal_id}",
            json=error)
        response.raise_for_status()

