""""
Test cases for list friends function
"""

import unittest
from schemas import validate_single_email
from jsonschema import ValidationError
from managefriends import list_friends_request


class ListFriendsTest(unittest.TestCase):
    def setUp(self):
        self.friends_empty = {

        }

        self.friends_sample_no_friends = {
            'andy@example.com': []
        }

        self.friends_sample_two_emails = {
            'andy@example.com': ["john@example.com", "snow@example.com"]
        }

    #wrong json format
    def test_wrong_json_format(self):
        wrong_json = { "invalid json" }
        with self.assertRaises(ValidationError):
            validate_single_email(wrong_json)

    #wrong field present in json
    def test_wrong_field(self):
        wrong_json_field = { "enemies" : "andy@example.com"}
        with self.assertRaises(ValidationError):
            validate_single_email(wrong_json_field)

    #wrong email format
    def test_wrong_email(self):
        wrong_json_email = { "email": "andy" }
        with self.assertRaises(ValidationError):
            validate_single_email(wrong_json_email)

    #check friends list without user email
    def test_successful_list_friends_where_email_not_present_in_dictionary(self):
        json_req = { "email" : "andy@example.com" }
        actual_json = list_friends_request(json_req, self.friends_empty)
        expected_json = {"success": True, "friends": [], "count": 0}
        self.assertEqual(expected_json, actual_json)

    #check friends list with user email, who has no friends
    def test_successful_list_friends_with_email_present_in_dictionary_no_friends(self):
        json_req = { "email" : "andy@example.com" }
        actual_json = list_friends_request(json_req, self.friends_sample_no_friends)
        expected_json = {"success": True, "friends": [], "count": 0}
        self.assertEqual(expected_json, actual_json)

    #check friends list with user email
    def test_successful_list_friends_user_has_friends(self):
        json_req = { "email" : "andy@example.com" }
        actual_json = list_friends_request(json_req, self.friends_sample_two_emails)
        expected_json = {"success": True, "friends": ["john@example.com", "snow@example.com"], "count": 2}
        self.assertEqual(expected_json, actual_json)

if __name__ == '__main__':
    unittest.main()
