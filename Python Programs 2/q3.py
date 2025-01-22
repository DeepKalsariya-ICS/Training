# Create a menu driven program for managing operations that are given below.

# Menuitem:
# Display My Number
# Add into My Number
# Subtract from My Number
# Multiply with My Number
# Divide My Number
# 	Note : 
# ‘My Number’ will be default number which will be initially zero(0) when the program will start its execution.
# After performing the operation the result must be displayed and stored in ‘My Number’ variable(or object) so it can be displayed at any time from the menu.

number = 0

def display_num():
    print("Number: ", number)

def add_num():
    n = int(input("What number you want to add: "))
    global number
    number += n

def sub_num():
    n = int(input("What number you want to subtract: "))
    global number
    number -= n

def mul_num():
    n = int(input("What number you want to multiply: "))
    global number
    number *= n

def devide_num():
    n = int(input("What number you want to devide: "))
    global number
    number /= n

def my_menu():
    while True:
        print("\nMenu Items: ")
        print("1. Display Number: ")
        print("2. Add into Number: ")
        print("3. Subtract from Number: ")
        print("4. Multiply with Number: ")
        print("5. Divide Number: ")
        
        choice = int(input("\nPress Enter if you want to exit the program.\nChoose one option:"))
        if not choice: break
        if choice == 1: display_num()
        elif choice == 2: add_num()
        elif choice == 3: sub_num()
        elif choice == 4: mul_num()
        elif choice == 5: devide_num()
        else: 
            print("You made invalid choice!")
        print("-"*100)

my_menu()