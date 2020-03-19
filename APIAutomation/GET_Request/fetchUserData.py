import requests
import json
import jsonpath

# API URL

url = "https://reqres.in/api/users?page=2"

# Send get request

response = requests.get(url)
# print(response.text)

# Display response content

# print(response.content)
# print(response.headers)

# Parse response to json format
json_response = json.loads(response.text)
# print(json_response)

# fetch value using json path

pages = jsonpath.jsonpath(json_response, 'total_pages')
# print(pages[0])
assert pages[0] == 2