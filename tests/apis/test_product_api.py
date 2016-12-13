from test_base import BaseTestCase
from factories.product_factory import ProductFactory
from app.models.product import Product


class ProductApiTests(BaseTestCase):

    def setUp(self):
        ProductFactory.create_batch(10)

    def tearDown(self):
        Product.query.delete()

    def test_should_respond_ok_to_product_path(self):
        response = self.client.get("/api/product/")
        self.assert_200(response)

    def test_json_should_column_and_data(self):
        response = self.client.get("/api/product/")
        assert "columns" in response.json
        assert "data" in response.json

    def test_json_columns_should_have_product_and_value(self):
        response = self.client.get("/api/product/")
        assert "product" in response.json["columns"]
        assert "value" in response.json["columns"]

    def test_json_return_10_products(self):
        response = self.client.get("/api/product/")
        self.assertEqual(len(response.json['data']), 10)
