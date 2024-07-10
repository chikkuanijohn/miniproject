#Doctor Appointment Booking System
appointment_ids = []
patient_names = []
appointment_dates = []
doctor_names = []
def book_appointment(appointment_id, patient_name, appointment_date, doctor_name):
    appointment_ids.append(appointment_id)
    patient_names.append(patient_name)
    appointment_dates.append(appointment_date)
    doctor_names.append(doctor_name)
    print(f"Appointment booked successfully for {patient_name} with Dr. {doctor_name} on {appointment_date}.")
def cancel_appointment(appointment_id):
    if appointment_id in appointment_ids:
        index = appointment_ids.index(appointment_id)
        del appointment_ids[index]
        del patient_names[index]
        del appointment_dates[index]
        del doctor_names[index]
        print(f"Appointment with ID {appointment_id} has been cancelled.")
    else:
        print(f"No appointment found with ID {appointment_id}.")
def view_appointments():
    if appointment_ids:
        print("All Appointments:")
        for i in range(len(appointment_ids)):
            print(f"ID: {appointment_ids[i]}, Patient: {patient_names[i]}, Date: {appointment_dates[i]}, Doctor: {doctor_names[i]}")
    else:
        print("No appointments found.")
while True:
    print("\nDoctor Appointment Booking System")
    print("1. Book Appointment")
    print("2. Cancel Appointment")
    print("3. View Appointments")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        appointment_id = input("Enter Appointment ID: ")
        patient_name = input("Enter Patient Name: ")
        appointment_date = input("Enter Appointment Date (YYYY-MM-DD): ")
        doctor_name = input("Enter Doctor Name: ")
        book_appointment(appointment_id, patient_name, appointment_date, doctor_name)

    elif choice == '2':
        appointment_id = input("Enter Appointment ID to cancel: ")
        cancel_appointment(appointment_id)

    elif choice == '3':
        view_appointments()

    elif choice == '4':
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

                
    
        
    
            

            
            

        
        



