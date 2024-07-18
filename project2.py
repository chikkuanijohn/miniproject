from users import*
from booking import*

def main():
    while True:
        print("\n--- Cab Booking System ---")
        print("1. Register")
        print("2. Login")
        print("3. Book a Cab")
        print("4. View Bookings")
        print("5. Cancel Booking")
        print("6. Exit")
        ch = input("Enter your choice: ")

        if ch == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(register_user(username, password))
        
        elif ch== '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(login_user(username, password))
        
        elif ch == '3':
            username = input("Enter username: ")
            origin = input("Enter origin: ")
            destination = input("Enter destination: ")
            print(book_cab(username, origin, destination))
        
        elif ch == '4':
            username = input("Enter username: ")
            bookings = view_bookings(username)
            if bookings:
                # for b in bookings:
                print(f"Booking ID: {bookings['id']}, Origin: {bookings['origin']}, Destination: {bookings['destination']}")
            else:
                print("No bookings found.")
        
        elif ch == '5':
            username = input("Enter username: ")
            booking_id = int(input("Enter booking ID: "))
            print(cancel_booking(username, booking_id))
        
        elif ch== '6':
            print("Exiting system.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()