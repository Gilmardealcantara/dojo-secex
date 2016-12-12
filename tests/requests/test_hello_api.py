from test_base import BaseTestCase


class HelloApiTests(BaseTestCase):

    def test_should_respond_ok_to_hello_path(self):
        response = self.client.get("/api/hello/")
        self.assert_200(response)

    def test_should_respond_hello_in_a_json(self):
        response = self.client.get('/api/hello/')
        self.assertEqual('application/json', response.headers['content-type'])
        self.assertIn('hello', response.json)
