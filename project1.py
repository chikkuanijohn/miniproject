def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1.add \n 2.sub \n 3.mul \n 4.div \n")
    

    while True:
        choice = input("Enter choice (1/2/3/4) or 'q' to quit: ")
        
        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == 'q':
            print("Exiting the calculator")
            break
        else:
            print("Invalid input. Please enter a valid choice.")
calculator()

                
    
        
    
            

            
            

        
        



