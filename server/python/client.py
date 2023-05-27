import requests
import json

data = {
    "FirstName": "Joanne",
    "LastName": "Leow",
    "Email": "feranmi.ayo@example.com",
    "PhoneNo": "+3234567890",
    "Dob": "1993-01-01",
    "Address": "123 Leow Street, City, Country",
    "Password": "password123",
}

# data = {
#     "Email": "feranmi.ayo@example.com",
#     "Password": "password1234",
# }
headers = {
    "content-type": "application/json"
}

req = requests.post("http://127.0.0.1:5000/register",
                    headers=headers,
                    data=json.dumps(data))

# req = requests.post("http://127.0.0.1:5000/remove-user",
#                     headers=headers,
#                     data=json.dumps(data))

# req = requests.delete("http://127.0.0.1:5000/user/68f74885-145e-4561-be35-e071d36ffb5f")
# Checking the response
if req.status_code == 200:
    print('POST request was successful!')
else:
    print(f'POST request failed with status code: {req.status_code}')
