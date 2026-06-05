class Bus:
    def __init__(self, route, total_seats):
        self.route = route
        self.total_seats = total_seats
        self.booked = {}
    
    def book_seat(self, seat_number, passenger_name):
        if seat_number in self.booked: #if already found in self.book then dont show again
            print(f"Seat {seat_number} already booked")
        else:
            self.booked[seat_number] = passenger_name
            print(f"Seat {seat_number}  booked for {passenger_name}.")

    def available_seats(self):
        return self.total_seats - len(self.booked)

    def passenger_list(self):
        print('---- Passenger List-----')
        for seat, name in sorted(self.booked.items()):
            print(f"Seat {seat}: {name}")
        print(f"Available seats:{self.available_seats()}")

bus = Bus('Kathmandu - Pokhara',10)
bookings= [
    (3, 'Ashim Acharya'),
    (7, 'Hom Nath Acharya'),
    (8, 'Manogy Guragain'),
]

for seat, name in bookings: #eg seat=3 and Name= Ashim Acharya
    bus.book_seat(seat, name)
bus.passenger_list()

