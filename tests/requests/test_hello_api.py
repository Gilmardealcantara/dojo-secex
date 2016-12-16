from test_base import BaseTestCase


class HelloApiTests(BaseTestCase):

    def test_should_respond_ok_to_hello_path(self):
        response = self.client.get("/api/product/")
        self.assert_200(response)
