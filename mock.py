import unittest
from unittest.mock import Mock
from unittest.mock import patch
#
# class Test_API(unittest.TestCase):
#     # Create a fake (mock) object
#     fake_api = Mock()
#
#
#     # Make it return a fixed value
#     fake_api.get_data.return_value = {"temp": 25}
#
#
#     # Use the mock instead of the real API
#     def test_weather_api(self):
#         result = self.fake_api.get_data()
#         assert result == {"temp": 25}  # Passes (no real API call!)


#     def get_user_name(user_id):
#         # Imagine this calls a real database
#         return "Alice"
#
#         # Override the function with a mock during the test
#
#     with patch("module.get_user_name") as mock_get_user:
#         mock_get_user.return_value = "Bob"  # Fake response
#         assert get_user_name(123) == "Bob"  # Uses mock, not real DB
# import unittest
# from unittest.mock import Mock, patch
# #
# def send_email(to, message):
#     # Imagine this sends a real email
#     print(f"Email to {to}: {message}")
#
# def notify_user(to, message):
#     # In real code this would call send_email()
#     send_email(to, message)
#
# def get_user_name(user_id):
#     """Real function that would query a database."""
#     return "Alice"
#
# class TestAPI(unittest.TestCase):
#     def setUp(self):
#         self.fake_api = Mock()
#         self.fake_api.get_data.return_value = {"temp": 25}
#
#     def test_weather_api_with_mock_object(self):
#         result = self.fake_api.get_data()
#         self.assertEqual(result, {"temp": 25})
# #
#     @patch('mockexamplefile.get_user_name')      # Patch the function in this module
#     def test_get_user_name_with_patch(self, mock_get_user):
#         mock_get_user.return_value = "Bob"
#         result = get_user_name(123)    # Calls the mocked version
#         self.assertEqual(result, "Bob")
#
#     @patch('mockexamplefile.notify_user')
#     @patch('mockexamplefile.send_email')  # ✅ target matches your new filename
#     def test_send_email_with_patch(self, mock_send):  # ✅ now accepts the mock
#         notify_user("user@test.com", "Hello!")
#         mock_send.assert_called_with("user@test.com", "Hello!")

#
# if __name__ == '__main__':
#     unittest.main()


import unittest
from unittest.mock import Mock, patch

def send_email(to, message):
    print(f"Email to {to}: {message}")

def notify_user(to, message):
    send_email(to, message)

def get_user_name(user_id):
    return "Alice"

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.fake_api = Mock()
        self.fake_api.get_data.return_value = {"temp": 25}

    def test_weather_api_with_mock_object(self):
        result = self.fake_api.get_data()
        self.assertEqual(result, {"temp": 25})

    @patch('mockexamplefile.get_user_name')
    def test_get_user_name_with_patch(self, mock_get_user):
        mock_get_user.return_value = "Bob"
        result = get_user_name(123)
        self.assertEqual(result, "Bob")

    @patch('mockexamplefile.send_email')          # only patch send_email
    def test_send_email_with_patch(self, mock_send):
        notify_user("user@test.com", "Hello!")
        mock_send.assert_called_with("user@test.com", "Hello!")

if __name__ == '__main__':
    unittest.main()