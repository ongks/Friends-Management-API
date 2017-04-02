""""
Test cases for subscribing to updates function
"""

import unittest
from schemas import validate_requestor_target
from jsonschema import ValidationError
from managefriends import sub_updates_request


class SubscribeUpdateTest(unittest.TestCase):
    def setUp(self):
        self.get_updates_empty = {

        }

        self.get_updates_sample_emails = {
            'lisa@example.com': ["snow@example.com"],
            'john@example.com': ["snow@example.com"]
        }

        self.block_empty = {

        }
        self.block_target = {
            'lisa@example.com': ["john@example.com"]
        }

        self.block_requestor = {
            'john@example.com': ["lisa@example.com"]
        }

    # wrong json format
    def test_wrong_json_format(self):
        wrong_json = {"invalid json"}
        with self.assertRaises(ValidationError):
            validate_requestor_target(wrong_json)

    # wrong field present in json
    def test_wrong_field(self):
        wrong_json_field = {"enemies": 'andy@example.com', "friends" : 'john@example.com'}
        with self.assertRaises(ValidationError):
            validate_requestor_target(wrong_json_field)

    # wrong email format
    def test_wrong_email(self):
        wrong_json_email = {"requestor": "lisa", "target": "john"}
        with self.assertRaises(ValidationError):
            validate_requestor_target(wrong_json_email)

    # check whether new emails is added to get updates dict
    def test_successful_sub_updates_empty_dict(self):
        json_req = {"requestor": "lisa@example.com", "target": "john@example.com"}
        sub_updates_request(json_req, self.get_updates_empty, self.block_empty)
        expected_dict = {'lisa@example.com': ['john@example.com']}
        self.assertDictEqual(expected_dict, self.get_updates_empty)

    def test_successful_sub_updates_empty_dict_json(self):
        json_req = {"requestor": "lisa@example.com", "target": "john@example.com"}
        actual_json = sub_updates_request(json_req, self.get_updates_empty, self.block_empty)
        expected_json = {"success": True}
        self.assertEqual(expected_json, actual_json)

    # target is on user's block list
    def test_user_block_other(self):
        json_req = {"requestor": "lisa@example.com", "target": "john@example.com"}
        sub_updates_request(json_req, self.get_updates_empty, self.block_target)
        expected_dict = {'lisa@example.com': []}
        self.assertDictEqual(expected_dict, self.get_updates_empty)

    def test_user_block_other_json(self):
        json_req = {"requestor": "lisa@example.com", "target": "john@example.com"}
        actual_json = sub_updates_request(json_req, self.get_updates_empty, self.block_target)
        expected_json = {"success": False, "message": "Requested user has been blocked."}
        self.assertEqual(expected_json, actual_json)

    # user is on target's block list
    def test_blocked_by_other_user(self):
        json_req = {"requestor": "lisa@example.com", "target": "john@example.com"}
        sub_updates_request(json_req, self.get_updates_empty, self.block_requestor)
        expected_dict = {'lisa@example.com': ['john@example.com']}
        self.assertDictEqual(expected_dict, self.get_updates_empty)

    def test_blocked_by_other_user_json(self):
        json_req = {"requestor": "lisa@example.com", "target": "john@example.com"}
        actual_json = sub_updates_request(json_req, self.get_updates_empty, self.block_requestor)
        expected_json = {"success": True}
        self.assertEqual(expected_json, actual_json)

    # user is already present in get updates dict
    def test_successful_sub_updates_req_present_in_dict(self):
        json_req = {"requestor": "lisa@example.com", "target": "john@example.com"}
        sub_updates_request(json_req, self.get_updates_sample_emails, self.block_empty)
        expected_dict = {'lisa@example.com': ['snow@example.com', 'john@example.com'], 'john@example.com': ["snow@example.com"]}
        self.assertDictEqual(expected_dict, self.get_updates_sample_emails)

    def test_successful_sub_updates_req_present_in_dict_json(self):
        json_req = {"requestor": "lisa@example.com", "target": "john@example.com"}
        actual_json = sub_updates_request(json_req, self.get_updates_sample_emails, self.block_empty)
        expected_json = {"success": True}
        self.assertEqual(expected_json, actual_json)

if __name__ == '__main__':
    unittest.main()
