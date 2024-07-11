#Doctor Appointment Booking System
users = []
appointments = []
def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = [username, password]
    users.append(user)
    print("User registered successfully!")
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    for user in users:
        if user[0] == username and user[1] == password:
            print("Login successful!")
            return True
    print("Invalid username or password!")
    return False
def book_appointment():
    if login():
        name = input("Enter your name: ")
        date = input("Enter appointment date: ")
        time = input("Enter appointment time: ")
        doctor = input("Enter doctor's name: ")
        appointment = [name, date, time, doctor]
        appointments.append(appointment)
        print("Appointment booked successfully!")
def display_appointments():
    if login():
        for appointment in appointments:
            print("Name:", appointment[0])
            print("Date:", appointment[1])
            print("Time:", appointment[2])
            print("Doctor:", appointment[3])
            print("---")
while True:
    print("1. Register")
    print("2. Login")
    print("3. Book Appointment")
    print("4. Display Appointments")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        book_appointment()
    elif choice == "4":
        display_appointments()
    elif choice == "5":
        print("exiting  the system.Goodbye")
        break
    else:
        print("Invalid choice")
