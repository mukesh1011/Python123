import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users"

# Read input json file
file = open('/home/mukesh/Python123/APIAutomation/createUser.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)

# Make Post Request with json input body

response = requests.post(url, request_json)

# Validating response code
assert response.status_code == 201

# Fetch header from response
print(response.headers)

# Parse response to json format
response_json = json.loads(response.text)

# Pick id using json path
id = jsonpath.jsonpath(response_json,'id')
print(id[0])