from user import User

import datetime

data = {
    "1990-01-01",
    "+1234567890",
    "password123",
    "emina.ergul@example.com",
    "123 Main Street, City, Country",
    "Ergul",
    "Emina",
}

u_id = "6ea633e3-87f8-4807-bd16-2bdba0a8869b"

login1 = {
    "Email": "emina.ergul@example.com",
    "Password": "password123",
}

login2 = {
    "Email": "feranmi.ayo@example.com",
    "Password": "password1234",
}

user_one = User(
    "Emina",
    "Ergul",
    "emina.ergul@example.com",
    "+1234567890",
    "1990-01-01",
    "123 Main Street, City, Country",
    "password123",
)

register_data = {
    "FirstName": "Joanne",
    "LastName": "Leow",
    "Email": "feranmi.ayo@example.com",
    "PhoneNo": "+3234567890",
    "Dob": "1993-01-01",
    "Address": "123 Leow Street, City, Country",
    "Password": "password123",
}

output = {
    "FirstName": "Joanne",
    "LastName": "Leow",
    "Email": "feranmi.ayo@example.com",
    "PhoneNo": "+3234567890",
    "Dob": "1993-01-01",
    "Address": "123 Leow Street, City, Country",
    "Password": "password123",
    "status": "success",
    "message": "user added successfully",
}

users = [
    {
        "Address": "123 Leow Street, City, Country",
        "Dob": datetime.date(1993, 1, 1),
        "Email": "feranmi.ayo@example.com",
        "FirstName": "Joanne",
        "LastName": "Leow",
        "Password": "$2b$12$4IiNAiLp.rs0CeP7eJhuL.NQj0O7.R17riyO.6NAD/hdn/KIfGb7q",
        "PhoneNo": "+3234567890",
        "UserId": "0c92f4af-234e-4437-800c-38496d0f0dc6",
    }
]
