from test_base import BaseTestCase


class ProductApiTests(BaseTestCase):

    def test_should_respond_ok_to_product_path(self):
        response = self.client.get("/api/product/")
        self.assert_200(response)

    def test_json_should_column_and_data(self):
        response = self.client.get("/api/product/")
        assert "columns" in response.json
        assert "data" in response.json
