# Add a dictionaries from user in such a way to get below output.Merge keys of dictionary and manage values accordingly

# {52: {'march': 1, 'may': 2, 'june': 3, 'july': 1, 'feb': 0, 'aug': 2, 'jan': 0, 'april': 5, 'November': 1, 'dec': 0, 'sept': 0, 'oct': 0}},
# {52: {'march': 0, 'may': 0, 'june': 0, 'july': 0, 'feb': 0, 'aug': 0, 'jan': 0, 'april': 0, 'November': 1, 'dec': 0, 'sept': 0, 'oct': 0}},
# {51: {'march': 0, 'may': 1, 'june': 0, 'july': 0, 'feb': 8, 'aug': 0, 'jan': 0, 'april': 2, 'November': 1, 'dec': 0, 'sept': 0, 'oct': 0}},
# {48: {'march': 0, 'may': 0, 'june': 4, 'july': 0, 'feb': 0, 'aug': 0, 'jan': 0, 'april': 3, 'November': 1, 'dec': 0, 'sept': 0, 'oct': 0}},
# {48: {'march': 0, 'may': 0, 'june': 0, 'july': 0, 'feb': 4, 'aug': 0, 'jan': 1, 'april': 0, 'November': 1, 'dec': 0, 'sept': 0, 'oct': 0}}]

# to create sub dict of list
def make_sub_dict():
    dict = {}
    keys = ["march", "may", "june", "july", "feb", "aug", "jan", "april", "November", "dec", "sept", "oct"]
    for key in keys:
        value = int(input(f"Enter value for {key}:  "))
        dict[key] = value 
    return dict

# create list with dict elements in it
list01 = []
while True:
    dict_i = {}
    ip = input("\nEnter key of dictionary.\nOr to stop program just press enter: ")
    print()
    if not ip:
        print("\tYou Entered Nothing!")
        break
    sub_dict = make_sub_dict()
    dict_i[ip] = sub_dict
    list01.append(dict_i)

print()

# Display input list
for element in list01:
    print(element)


# find index of elements having same key
list_of_same = []
for i in range(len(list01)):
    for j in range(i+1, len(list01)):
        if list01[i].keys() == list01[j].keys():
            list_of_same.append((i, j))

# add values of elements having same key
for i, j in list_of_same:
    v1 = list01[i].values()
    v2 = list01[j].values()
    for i in v1:
        v1 = i
    for i in v2:
        v2 = i
    keys = ["march", "may", "june", "july", "feb", "aug", "jan", "april", "November", "dec", "sept", "oct"]
    for key in keys:
        v1[key]+=v2[key]    

# remove element that has same key
list_of_same.reverse()
for i, j in list_of_same:
    list01.pop(j)    

print()
# Display final list
for element in list01:
    print(element)