# method II for serialization
# dump write json to file without converting to an object first
import json

# Data to be written
dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}

with open("sample.json", "w") as outfile:
    json.dump(dictionary, outfile)
