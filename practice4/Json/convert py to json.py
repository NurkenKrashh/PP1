import json

data = {
    "name": "Nurken",
    "age": 17,
    "is_student": True
}

json_string = json.dumps(data)

print(json_string)
print(type(json_string))