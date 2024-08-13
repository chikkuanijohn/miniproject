import sqlite3

con = sqlite3.connect("medical_store.db")
cursor = con.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS medical (
    id INTEGER PRIMARY KEY,
    name TEXT,
    quantity INTEGER,
    price REAL
)""")

con.commit()

def add_medical():
    try:
        name = input('Enter medicine name: ')
        quantity = int(input('Enter quantity: '))
        price = float(input('Enter price: '))
        cursor.execute('INSERT INTO medical (name, quantity, price) VALUES (?, ?, ?)', (name, quantity, price))
        con.commit()
        print("Medicine added successfully!")
    except Exception as e:
        print("Error:", e)

def update_medical():
    try:
        id = int(input('Enter medicine ID: '))
        name = input('Enter new name: ')
        quantity = int(input('Enter new quantity: '))
        price = float(input('Enter new price: '))
        cursor.execute('UPDATE medical SET name = ?, quantity = ?, price = ? WHERE id = ?', (name, quantity, price, id))
        con.commit()
        print("Medicine updated successfully!")
    except Exception as e:
        print("Error:", e)

def delete_medical():
    try:
        id = int(input('Enter medicine ID: '))
        cursor.execute('DELETE FROM medical WHERE id = ?', (id,))
        con.commit()
        print("Medicine deleted successfully!")
    except Exception as e:
        print("Error:", e)

def view_medical():
    try:
        cursor.execute('SELECT * FROM medical')
        medical = cursor.fetchall()
        print("ID\tName\tQuantity\tPrice")
        for med in medical:
            print(f"{med[0]}\t{med[1]}\t{med[2]}\t{med[3]}")
    except Exception as e:
        print("Error:", e)

while True:
    print('1. Add medical')
    print('2. Update medical')
    print('3. Delete medical')
    print('4. View medical')
    print('5. Quit')
    ch = input('Enter choice: ')
    if ch == '1':
        add_medical()
    elif ch == '2':
        update_medical()
    elif ch == '3':
        delete_medical()
    elif ch == '4':
        view_medical()
    elif ch == '5':
        break
    else:
        print('Invalid choice')


