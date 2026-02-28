import json


with open("sample-data.json", "r") as file:
    data = json.load(file)


for student in data["students"]:
    print(student["name"])

data["students"].append({
    "name": "Arman",
    "age": 16,
    "grades": [80, 82, 85]
})

with open("sample-data.json", "w") as file:
    json.dump(data, file, indent=4)