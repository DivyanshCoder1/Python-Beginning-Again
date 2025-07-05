import os
booked_seat_numbers = []
booked_dict = {}

class Train:
    def __init__(self,name,seat_no):
        if seat_no in booked_seat_numbers:
            print(f"{seat_no} is already booked, The following seats are available: ")
            for i in range(1,73):
                if i in booked_seat_numbers:
                    continue
                else:
                    print(i, end = " ")
        elif seat_no > 72 or seat_no < 1:
            print("Sorry, there are only 72 seats in the train!")
        else:
            self.name = name
            self.seat_no = seat_no
            booked_dict[seat_no] = self.name
            booked_seat_numbers.append(seat_no)
            print("Seat Successfully booked!!")


    def get_status(seat_no):
        if seat_no in booked_seat_numbers:
            print("Status: [RESERVED]")
            print("Passenger: ", booked_dict[seat_no])
        elif seat_no > 72 or seat_no < 1:
            print("Status: [NON-EXISTENT]")
        else:
            print("Status: [UNRESERVED]")
    
    def get_fare(seat_no):
        if seat_no in booked_seat_numbers:
            print("Status: [RESERVED]")
            print("Cannot fetch status of a reserved seat")
        elif seat_no > 72 or seat_no < 1:
            print("Seat do not exist")
        else:
            print("Fare: 1000 ₹ / 15$")
    
    def cancel_ticket(self):
        if self.seat_no in booked_seat_numbers:
            del booked_dict[self.seat_no]
            booked_seat_numbers.remove(self.seat_no)
            print(f"Ticket for {self.name} has been cancelled!")
            print("Current Status: [UNRESERVED]")
        else:
            print("Seat is unreserved")
    
    def list_passengers():
        print("Seat No.    Name")
        for key in booked_dict.keys():
            print(key, " ", booked_dict[key])
    
    def list_seats():
        print("Available Seats: ")
        for i in range(1,73):
            if i in booked_seat_numbers:
                continue
            else:
                print(i, end= " ")

while True:
    print()
    print('''Class Name: Train
          >>Train.get_status(seat_no): get status of a seat
          >>Train.get_fare(seat_no): get fare for a seat
          >>Train.list_passengers(): List seats and passengers corresponding to them
          >>Train.list_seats(): Lists empty seats
          >>obj.cancel_ticket()''')
    print()
    user_input = input(">>> ")

    if user_input.lower() == "q":
        print("Exiting the simulation!")
        exit()
    else:
        try:
            exec(user_input)
        except Exception as e:
            try:
                eval(user_input)
            except Exception as ee:
                print("Error occured: ", ee)