bookings = []

def book_cab(username, origin, destination):
    booking_id = len(bookings) + 1
    booking = {
        'id': booking_id,
        'username': username,
        'origin': origin,
        'destination': destination
    }
    bookings.append(booking)
    users[username]['bookings'].append(booking)
    return f"Cab booked successfully! Booking ID: {booking_id}"

def view_bookings(username):
    return users[username]['bookings']

def cancel_booking(username, booking_id):
    for booking in bookings:
        if booking['id'] == booking_id and booking['username'] == username:
            bookings.remove(booking)
            users[username]['bookings'].remove(booking)
            return "Booking cancelled successfully!"
    return "Booking not found!"