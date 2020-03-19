import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users/2"

# Read input json file
file = open('/home/mukesh/Python123/APIAutomation/createUser.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)

# Make PUT Request with json input body

response = requests.put(url, request_json)

# Validating response code
assert response.status_code == 200

response_json = json.loads(response.text)
updated_li = jsonpath.jsonpath(response_json, 'updatedAt')

print(updated_li[0])