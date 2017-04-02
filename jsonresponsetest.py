"""
Simultaneously tests for working connection through use of dummy POST requests to each endpoint.
Also tests an example of invalid input to check that that a JSON response is received.
Full tests in respective functionality test.
"""
import unittest
from json import dumps, loads
from friendsapi import app


class JsonResponseTest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_invalid_json_add_friend(self):
        invalid_json = '{ "invalid json" }'
        response = self.app.post('/api/v0/addfriendrequest', data=dumps(invalid_json), content_type='application/json')
        data = loads(response.get_data(as_text=True))

        self.assertEqual(dumps(data), '{"message": "Invalid JSON request.", "success": false}')

    def test_invalid_json_list_friend(self):
        invalid_json = '{ "invalid json" }'
        response = self.app.post('/api/v0/listfriends', data=dumps(invalid_json), content_type='application/json')
        data = loads(response.get_data(as_text=True))

        self.assertEqual(dumps(data), '{"message": "Invalid JSON request.", "success": false}')


if __name__ == '__main__':
    unittest.main()
