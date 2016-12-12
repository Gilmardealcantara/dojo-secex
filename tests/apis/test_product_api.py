from test_base import BaseTestCase


class ProductApiTests(BaseTestCase):

    def test_should_respond_ok_to_product_path(self):
        response = self.client.get("/api/product/")
        self.assert_200(response)