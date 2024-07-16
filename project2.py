from user import*
from book_cab import*

def main():
    while True:
        print("\n--- Cab Booking System ---")
        print("1. Register")
        print("2. Login")
        print("3. Book a Cab")
        print("4. View Bookings")
        print("5. Cancel Booking")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(user.register_user(username, password))
        
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(user.login_user(username, password))
        
        elif choice == '3':
            username = input("Enter username: ")
            origin = input("Enter origin: ")
            destination = input("Enter destination: ")
            print(booking.book_cab(username, origin, destination))
        
        elif choice == '4':
            username = input("Enter username: ")
            bookings = cab_book.view_bookings(username)
            if bookings:
                for b in bookings:
                    print(f"Booking ID: {b['id']}, Origin: {b['origin']}, Destination: {b['destination']}")
            else:
                print("No bookings found.")
        
        elif choice == '5':
            username = input("Enter username: ")
            booking_id = int(input("Enter booking ID: "))
            print(booking.cancel_booking(username, booking_id))
        
        elif choice == '6':
            print("Exiting system.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "_main_":
    main()
