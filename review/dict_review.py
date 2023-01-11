this_dict = {'go': 'home', 'come': 'here', 'shift': 'away'}

# print the type of data
print(type(this_dict))

# Loop through the dictionary with a for loop
key = 0
while len(this_dict) > key:
    print(this_dict['go'])
    key += 1
