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


    def get_iata_codes(self):
        data = self.get_flight_data()

        for destination in data:
            iata = destination["iataCode"]
            self.iata_list.append(iata)

        return self.iata_list

    # def get_lowest_prices(self):
    #     lowest_price = {}
    #
    #     data = self.get_flight_data()
    #     for destination in data:
    #
    #     keys_to_extract = ['iataCode', 'lowestPrice']
    #     new_dict = {key: data[key] for key in keys_to_extract if key in data}
    #     return new_dict
