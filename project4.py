class Flight:
    def __init__(self, flight_number, origin, destination, departure_time, arrival_time):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.passengers = []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def get_details(self):
        return f"Flight {self.flight_number} from {self.origin} to {self.destination}, Departure: {self.departure_time}, Arrival: {self.arrival_time}"

class Passenger:
    def __init__(self, name, passport_number):
        self.name = name
        self.passport_number = passport_number

    def get_details(self):
        return f"Passenger {self.name}, Passport Number: {self.passport_number}"

class BookingSystem:
    def __init__(self):
        self.flights = []
        self.passengers = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def find_flight(self, flight_number):
        for flight in self.flights:
            if flight.flight_number == flight_number:
                return flight
        return None

    def find_passenger(self, passport_number):
        for passenger in self.passengers:
            if passenger.passport_number == passport_number:
                return passenger
        return None

    def book_ticket(self, flight_number, passport_number):
        flight = self.find_flight(flight_number)
        passenger = self.find_passenger(passport_number)
        if flight and passenger:
            flight.add_passenger(passenger)
            return f"Ticket booked for {passenger.name} on flight {flight.flight_number}"
        else:
            return "Flight or passenger not found"

# Example usage
if __name__ == "__main__":
    # Create a booking system
    booking_system = BookingSystem()

    # Create flights
    flight1 = Flight("AA101", "New York", "London", "2024-08-01 08:00", "2024-08-01 20:00")
    flight2 = Flight("BA202", "London", "Paris", "2024-08-02 09:00", "2024-08-02 11:00")

    # Add flights to the booking system
    booking_system.add_flight(flight1)
    booking_system.add_flight(flight2)

    # Create passengers
    passenger1 = Passenger("John thomas", "P12345678")
    passenger2 = Passenger("Martin ", "P87654321")

    # Add passengers to the booking system
    booking_system.add_passenger(passenger1)
    booking_system.add_passenger(passenger2)

    # Book tickets
    print(booking_system.book_ticket("AA101", "P12345678"))  
    print(booking_system.book_ticket("BA202", "P87654321"))  

    # Display flight details
    print(flight1.get_details())
    print(flight2.get_details())

    # Display passenger details
    print(passenger1.get_details())
    print(passenger2.get_details())
