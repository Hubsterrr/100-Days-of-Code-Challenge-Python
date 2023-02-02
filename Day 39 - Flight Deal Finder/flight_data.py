
#This class is responsible for structuring the flight data.

class FlightData:
    def __init__(self, flight_data):
        self.data = flight_data
        self.price = self.data["price"]
        self.departure_date = self.data['route'][0]['local_departure']
        self.return_date = self.data['route'][1]['local_departure']
