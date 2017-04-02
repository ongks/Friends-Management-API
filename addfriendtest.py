""""
Test cases for add friends function
"""

import unittest
from schemas import validate_friends_pair
from jsonschema import ValidationError
from managefriends import add_friend_request


class AddFriendsTest(unittest.TestCase):
    def setUp(self):
        self.friends_empty = {

        }

        self.block_empty = {

        }

        self.get_updates_empty = {

        }

        self.friends_sample_emails = {
            'andy@example.com': ["john@example.com"],
            'john@example.com': ["andy@example.com"]
        }

        self.block_target = {
            'andy@example.com': ["john@example.com"]
        }

        self.block_requestor = {
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
        wrong_json_email = { "friends": ['andy', 'bob' ]}
        with self.assertRaises(ValidationError):
            validate_friends_pair(wrong_json_email)



    #check whether new emails are added to the friends and getupdates dict
    def test_successful_add_friends_to_friends_dict(self):
        json_req = { "friends" : ['andy@example.com', 'john@example.com']}
        add_friend_request(json_req, self.friends_empty, self.get_updates_empty, self.block_empty)
        expected_dict = {'andy@example.com' : ['john@example.com'], 'john@example.com' : ['andy@example.com']}
        self.assertDictEqual(expected_dict, self.friends_empty)

    def test_successful_add_friends_to_getupdates_dict(self):
        json_req = { "friends" : ['andy@example.com', 'john@example.com']}
        add_friend_request(json_req, self.friends_empty, self.get_updates_empty, self.block_empty)
        expected_dict = {'andy@example.com' : ['john@example.com'], 'john@example.com' : ['andy@example.com']}
        self.assertDictEqual(expected_dict, self.get_updates_empty)

    def test_successful_json(self):
        json_req = { "friends" : ['andy@example.com', 'john@example.com']}
        actual_json = add_friend_request(json_req, self.friends_empty, self.get_updates_empty, self.block_empty)
        expected_json = {"success": True}
        self.assertEqual(expected_json, actual_json)



    #target is on user's block list
    def test_friend_list_of_user_still_empty_when_blocked_target(self):
        json_req = { "friends" : ['andy@example.com', 'john@example.com']}
        add_friend_request(json_req, self.friends_empty, self.get_updates_empty, self.block_target)
        expected_dict = {'andy@example.com' : [], 'john@example.com' : []}
        self.assertDictEqual(expected_dict, self.friends_empty)

    def test_user_block_other(self):
        json_req = {"friends": ['andy@example.com', 'john@example.com']}
        actual_json = add_friend_request(json_req, self.friends_empty, self.get_updates_empty, self.block_target)
        expected_json = {"success": False, "message": "Requested user has been blocked."}
        self.assertEqual(expected_json, actual_json)


    #user is on target's block list
    def test_friend_list_of_user_still_empty_when_blocked_by_target(self):
        json_req = { "friends" : ['andy@example.com', 'john@example.com']}
        add_friend_request(json_req, self.friends_empty, self.get_updates_empty, self.block_requestor)
        expected_dict = {'andy@example.com' : [], 'john@example.com' : []}
        self.assertDictEqual(expected_dict, self.friends_empty)

    def test_blocked_by_other_user(self):
        json_req = {"friends": ['andy@example.com', 'john@example.com']}
        actual_json = add_friend_request(json_req, self.friends_empty, self.get_updates_empty, self.block_requestor)
        expected_json = {"success": False, "message": "You are blocked by the other user."}
        self.assertEqual(expected_json, actual_json)




    #already friends with each other
    def test_already_friends(self):
        json_req = {"friends": ['andy@example.com', 'john@example.com']}
        actual_json = add_friend_request(json_req, self.friends_sample_emails, self.get_updates_empty, self.block_empty)
        expected_json = {"success": False, "message": "You are already friends with the user."}
        self.assertEqual(expected_json, actual_json)

if __name__ == '__main__':
    unittest.main()
