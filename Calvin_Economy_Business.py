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


class Business(Passenger):
    def __init__(self, name, location, destination, date, lounge_pass_code):
        super().__init__(name, location, destination, date)
        self.lounge_pass_code = lounge_pass_code

    def get_weight_allowance(self):
        return "100 kg"  # override
