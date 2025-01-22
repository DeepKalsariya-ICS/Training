# Write a python program to manage multiple values for the same key in dictionary.
# Enter key and value into dictionary.
# If the entered key already exist then do not overwrite the existing value of that key instead add both value into a list and place that list as a value of the entered key.


def make_dict():
    dict = {}
    while True:
        key = input("Enter Key: ")
        if not key:
            print("You entered nothing.\n")
            break
        value = input(f"Enter value for {key}: ")

        if key in dict and type(dict[key]) == list:
            dict[key].append(value)
        elif key in dict:
            ele = dict[key]
            v = [ele, value]
            dict[key] = v
        else:
            dict[key] = value
    print(f"Dictonary\n{dict}")

make_dict()