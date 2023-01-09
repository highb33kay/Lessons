# include json library
import json

# json string data
employee_string = '{"first_name": "Michael", "last_name": "Rodgers", "department": "Marketing"}'

# check data type with type() method
print(type(employee_string))

# convert string to  object
json_object = json.loads(employee_string)

# check new data type
print(type(json_object))

# access first_name in dictionary
print(json_object["first_name"])
