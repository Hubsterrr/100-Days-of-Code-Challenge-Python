# This class is responsible for structuring the flight data.

class FlightData:
    def __init__(self, flight_data):
        self.data = flight_data
        self.price = self.data["price"]
        self.departure_date = self.get_departure_date()
        self.return_date = self.get_return_date()

    def get_departure_date(self):
        departure_date_raw = self.data['route'][0]['local_departure']
        departure_date = departure_date_raw.replace("T", "      ")
        departure_date_format = departure_date.strip("Z")
        return departure_date_format

    def get_return_date(self):
        return_date_raw = self.data['route'][1]['local_departure']
        return_date = return_date_raw.replace("T", "      ")
        return_date_format = return_date.strip("Z")
        return return_date_format
