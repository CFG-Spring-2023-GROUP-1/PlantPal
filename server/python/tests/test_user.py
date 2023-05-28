import unittest
from unittest import TestCase, mock
from unittest.mock import patch
import sys

sys.path.append("../")
from user import User
from constants import user_one, data, login1, login2, output, register_data, u_id, users


class TestUser(TestCase):
    def test_get_data(self):
        self.assertEqual(user_one.get_data(), data)
        self.assertTrue(user_one.get_data())

    @mock.patch("user.User.get_users")
    def test_users_exist(self, mock_users):
        mock_users.return_value = users
        result = User.get_users()
        assert len(result) > 0

    @mock.patch("user.User.get_users")
    def test_no_users_exist(self, mock_users):
        mock_users.return_value = []
        result = User.get_users()
        self.assertTrue(len(result) == 0)

    @mock.patch("user.User.get_user_id")
    def test_get_user_id(self, mock_user_id):
        mock_user_id.return_value = u_id
        result = user_one.get_user_id()
        self.assertEqual(result, u_id)
        self.assertTrue(result is not None)
        self.assertFalse(result is None)

    @mock.patch("user.User.get_user_id")
    def test_no_user_id(self, mock_id):
        mock_id.return_value = None
        result = user_one.get_user_id()
        self.assertFalse(result)

    @mock.patch("user.User.login")
    def test_login(self, mock_id):
        mock_id.return_value = user_one
        result = user_one.login(login1)
        self.assertTrue(result)

    @mock.patch("user.User.login")
    def test_incorrect_login(self, mock_id):
        mock_id.return_value = "Incorrect Username or Password"
        result = user_one.login(login2)
        self.assertEqual(result, "Incorrect Username or Password")

    @mock.patch("user.User.verify_password")
    def test_verify_password(self, mock_password):
        mock_password.return_value = "password123"
        result = user_one.verify_password()
        self.assertEqual(result, "password123")

    @mock.patch("user.User.verify_password")
    def test_wrong_password(self, mock_password):
        mock_password.return_value = "password123"
        result = user_one.verify_password()
        self.assertIsNot(result, "password124")

    @mock.patch("user.User.add_user")
    def test_add_user(self, mock_password):
        mock_password.return_value = output
        result = user_one.add_user(register_data)
        self.assertEqual(result, output)
