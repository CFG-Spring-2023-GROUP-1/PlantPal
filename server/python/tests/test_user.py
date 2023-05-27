import unittest
from unittest import TestCase, mock
from unittest.mock import patch
import sys
sys.path.append('../')
from user import User

data = {'1990-01-01', '+1234567890', 'password123', 'emina.ergul@example.com',
        '123 Main Street, City, Country', 'Ergul', 'Emina'}

u_id = '6ea633e3-87f8-4807-bd16-2bdba0a8869b'

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
output = {'FirstName': 'Joanne',
          'LastName': 'Leow',
          'Email': 'feranmi.ayo@example.com',
          'PhoneNo': '+3234567890',
          'Dob': '1993-01-01',
          'Address': '123 Leow Street, City, Country',
          'Password': 'password123', 'status': 'success',
          'message': 'user added successfully'}


class TestUser(TestCase):
    def test_get_data(self):
        self.assertEqual(user_one.get_data(), data)
        self.assertTrue(user_one.get_data())

    @staticmethod
    def test_users_exist():
        users = User.get_users()
        assert len(users) > 0

    def test_no_users_exist(self):
        users = User.get_users()
        self.assertTrue(len(users))

    def test_get_user_id(self):
        self.assertEqual(user_one.get_user_id(), u_id)
        self.assertTrue(user_one.get_user_id())
        self.assertFalse(not user_one.get_user_id())

    @mock.patch('user.User.get_user_id')
    def test_no_user_id(self, mock_id):
        mock_id.return_value = None
        result = user_one.get_user_id()
        self.assertFalse(result)

    @mock.patch('user.User.login')
    def test_login(self, mock_id):
        mock_id.return_value = user_one
        result = user_one.login(login1)
        self.assertTrue(result)

    @mock.patch('user.User.login')
    def test_incorrect_login(self, mock_id):
        mock_id.return_value = 'Incorrect Username or Password'
        result = user_one.login(login2)
        self.assertEqual(result, 'Incorrect Username or Password')

    @mock.patch('user.User.verify_password')
    def test_verify_password(self, mock_password):
        mock_password.return_value = 'password123'
        result = user_one.verify_password()
        self.assertEqual(result, 'password123')

    @mock.patch('user.User.verify_password')
    def test_wrong_password(self, mock_password):
        mock_password.return_value = 'password123'
        result = user_one.verify_password()
        self.assertIsNot(result, 'password124')

    @mock.patch('user.User.add_user')
    def test_add_user(self, mock_password):
        mock_password.return_value = output
        result = user_one.add_user(register_data)
        self.assertEqual(result, output)

