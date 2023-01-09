# iterate over a json file using the iter() function
# import json
import json

with open('data.json') as f:
    data_list = json.load(f)

# # convert the json data to a list
# data_list = list(data)

# use the iter() function to create an iterator over the data
for item in iter(data_list):
    next(data_list[item])
