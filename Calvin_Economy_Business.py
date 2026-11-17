# Activity II - Airline Ticket Booking System
# Calvin - Child Classes: Economy & Business
# (Extends Deng's Passenger base class; paste below Deng's code in the final file)


class Economy(Passenger):
    def __init__(self, name, location, destination, date, seat_preference):
        super().__init__(name, location, destination, date)
        self.seat_preference = seat_preference

    def get_passenger_info(self):
        base_info = super().get_passenger_info()
        return base_info + f"\nSeat Preference: {self.seat_preference}\n---------------------------"
