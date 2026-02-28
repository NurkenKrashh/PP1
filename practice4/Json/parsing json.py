import json
json_string = '{"name":"Nurken" , "age":17 }'
data = json.loads(json_string)
print(data)
print(type(data))