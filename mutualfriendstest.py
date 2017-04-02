""""
Test cases for list mutual friends function
"""

import unittest
from schemas import validate_friends_pair
from jsonschema import ValidationError
from managefriends import list_mutual_friends_request


class ListFriendsTest(unittest.TestCase):
    def setUp(self):
        self.friends_empty = {

        }

        self.friends_two_mutual_friends = {
            'andy@example.com': ["john@example.com", "snow@example.com", "lola@example.com"],
            'john@example.com': ["lola@example.com", "snow@example.com", "andy@example.com"]
        }

        self.friends_no_mutual_friends = {
            'andy@example.com': ["john@example.com"],
            'john@example.com': ["andy@example.com"]
        }

    #wrong json format
    def test_wrong_json_format(self):
        wrong_json = { "invalid json" }
        with self.assertRaises(ValidationError):
            validate_friends_pair(wrong_json)

    #wrong field present in json
    def test_wrong_field(self):
        wrong_json_field = { "enemies" : ['andy@example.com', 'john@example.com']}
        with self.assertRaises(ValidationError):
            validate_friends_pair(wrong_json_field)

    #wrong email format
    def test_wrong_email(self):
        wrong_json_email = { "friends": ['andy', 'bob']}
        with self.assertRaises(ValidationError):
            validate_friends_pair(wrong_json_email)

    #
    def test_successful_empty_friends_list(self):
        json_req = { "friends" : ['andy@example.com', 'john@example.com']}
        actual_json = list_mutual_friends_request(json_req, self.friends_empty)
        expected_json = {"success": True, "friends": [], "count": 0}
        self.assertEqual(expected_json, actual_json)

    #check friends list with user email, who has no friends
    def test_successful_no_mutual_friends(self):
        json_req = { "friends" : ['andy@example.com', 'john@example.com']}
        actual_json = list_mutual_friends_request(json_req, self.friends_no_mutual_friends)
        expected_json = {"success": True, "friends": [], "count": 0}
        self.assertEqual(expected_json, actual_json)

    #check friends list with user email
    def test_successful_two_mutual_friends(self):
        json_req = { "friends" : ['andy@example.com', 'john@example.com']}
        actual_json = list_mutual_friends_request(json_req, self.friends_two_mutual_friends)
        expected_json = {"success": True, "friends": ["snow@example.com", "lola@example.com"], "count": 2}
        self.assertEqual(expected_json, actual_json)

if __name__ == '__main__':
    unittest.main()
