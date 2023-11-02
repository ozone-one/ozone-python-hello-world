import unittest
import json

from flask.wrappers import Response
from main import app

app.testing = True


class TestApi(unittest.TestCase):

    def test_main(self):
        with app.test_client() as client:
            # send data as POST form to endpoint
            sent = {'value': 11}
            result = client.post(
                '/',
                data=sent
            )
            # check result from server with expected data
            print(result.data, "here")
            self.assertEqual(
                result.data.decode('UTF-8'),
                json.dumps(sent)
            )
