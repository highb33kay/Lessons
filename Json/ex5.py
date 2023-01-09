# reading a json file called students
import json

with open('students.json', 'r') as f:
    data = json.load(f)
    print(type(data))
    print(data)
