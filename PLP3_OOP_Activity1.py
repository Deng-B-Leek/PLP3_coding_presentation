"""
PLP GROUP: PLP? - Airline Ticket Booking System - Activity 1 OOP

ROLE HEADER LOG (Proof of Contribution):
- Deng: Driver - Base Class Passenger, header log, file setup
- Calvin: Driver - Child Classes Economy, Business, FirstClass
- Luxe: Navigator - CLI Workflow Step 1 & 2 (Select Class + Base Data Entry)
- Adriel: Navigator - CLI Workflow Step 2 Dynamic Entry + Step 3 Summary + Error Handling
- Davina: Presenter - Integration, testing, video, submission
- Absent members: None
- Collaboration proof: VS Code Live Share screenshot + File passed in order Deng -> Calvin -> Luxe -> Adriel -> Davina
"""

# --- DENG - BASE CLASS ---
class Passenger:
    def __init__(self, name, location, destination, date):
        self.name = name
        self.location = location
        self.destination = destination
        self.date = date

    def get_passenger_info(self):
        return f"Passenger: {self.name} | From: {self.location} -> To: {self.destination} | Date: {self.date}"

    def get_weight_allowance(self):
        return 20

# --- CALVIN - CHILD CLASSES ---
class Economy(Passenger):
    def __init__(self, name, location, destination, date, seat_preference):
        super().__init__(name, location, destination, date)
        self.seat_preference = seat_preference

    def get_passenger_info(self):
        base = super().get_passenger_info()
        return f"{base} | Class: Economy | Seat Preference: {self.seat_preference}"

class Business(Passenger):
    def __init__(self, name, location, destination, date, lounge_pass_code, luggage_allowance=100):
        super().__init__(name, location, destination, date)
        self.lounge_pass_code = lounge_pass_code
        self.luggage_allowance = luggage_allowance

    def get_weight_allowance(self):
        return self.luggage_allowance

    def get_passenger_info(self):
        base = super().get_passenger_info()
        return f"{base} | Class: Business | Lounge Pass: {self.lounge_pass_code} | Luggage: {self.luggage_allowance} kg"

class FirstClass(Passenger):
    def __init__(self, name, location, destination, date, suite_number, chauffeur_service):
        super().__init__(name, location, destination, date)
        self.suite_number = suite_number
        self.chauffeur_service = chauffeur_service

    def get_passenger_info(self):
        base = super().get_passenger_info()
        chauffeur = "Yes" if self.chauffeur_service else "No"
        return f"{base} | Class: First Class | Suite: {self.suite_number} | Chauffeur: {chauffeur}"

# --- LUXE + ADRIEL - CLI + ERROR HANDLING ---
def get_valid_input(prompt):
    while True:
        value = input(prompt).strip()
        if value == "":
            print("Error: This field cannot be empty. Please try again.")
        else:
            return value

def main():
    print("=== Airline Ticket Booking System ===")
    print("[1] Economy")
    print("[2] Business")
    print("[3] First Class")

    while True:
        choice = input("Select Class (1-3): ").strip()
        if choice in ["1", "2", "3"]:
            break
        else:
            print("Error: Invalid choice. Please enter 1, 2, or 3.")

    print("\n--- Enter Passenger Details ---")
    name = get_valid_input("Enter name: ")
    location = get_valid_input("Enter location (From): ")
    destination = get_valid_input("Enter destination (To): ")
    date = get_valid_input("Enter date (YYYY-MM-DD): ")

    passenger = None
    if choice == "1":
        seat = get_valid_input("Enter seat preference (Window/Aisle): ")
        passenger = Economy(name, location, destination, date, seat)
    elif choice == "2":
        lounge = get_valid_input("Enter lounge pass code: ")
        passenger = Business(name, location, destination, date, lounge)
    elif choice == "3":
        suite = get_valid_input("Enter suite number: ")
        while True:
            chauffeur_input = input("Chauffeur service? (Yes/No): ").strip().lower()
            if chauffeur_input in ["yes", "y"]:
                chauffeur = True
                break
            elif chauffeur_input in ["no", "n"]:
                chauffeur = False
                break
            else:
                print("Error: Please type Yes or No.")
        passenger = FirstClass(name, location, destination, date, suite, chauffeur)

    print("\n=== Ticket Summary ===")
    print(passenger.get_passenger_info())
    print(f"Weight Allowance: {passenger.get_weight_allowance()} kg")
    print("Booking Confirmed!")

if __name__ == "__main__":
    main()