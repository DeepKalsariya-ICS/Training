# Write a python program to manage multiple employee details.
# Enter employee detail like name, mobile, email, birthdate, position, city
# Enter all that detail into dictionary and store that dictionary into a list until nothing is added.
# Example : [{‘name’:’Bhaskar’, ’mobile’:’987’},{}]
# Keep adding dictionary into list with new employee data.
# Print the employee detail into a tabular format given below.
from prettytable import PrettyTable

def enter_key_value():
    dict = {}
    keys = ["Name", "Mobile No", "Email", "City"]
    for key in keys:
        value = input(f"Enter value for {key}:  ")
        dict[key] = value 
    return dict

employee_details = []
while True:
    ip = input("\nEnter anything to contiue program execution.\nTo stop program just press enter: ")
    print()
    if not ip:
        print("\tYou Entered Nothing!")
        break
    employee_details.append(enter_key_value())
    
# Print employee details in table format
if employee_details:
    table = PrettyTable()
    table.field_names = ["Name", "Mobile No", "Email", "City"]
    for emp in employee_details:
        table.add_row([emp["Name"], emp["Mobile No"], emp["Email"], emp["City"]])
    print("\nEmployee Details:")
    print(table)
else:
    print("\nNo employee details to display.")

