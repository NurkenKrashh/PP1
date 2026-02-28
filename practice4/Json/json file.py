import json
data = {
    "name":"Nurken",
    "age" : 19,
    "is_student": True
}

with open("data.json", "w") as file:
    json.dump(data,file,indent=4)