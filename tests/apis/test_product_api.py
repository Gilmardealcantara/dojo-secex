from test_base import BaseTestCase
from factories.product_factory import ProductFactory
from app.models.product import Product
import logging

logging.getLogger("factory").setLevel(logging.WARN)


class ProductApiTests(BaseTestCase):

    def setUp(self):
        self.factory_products = ProductFactory.create_batch(10)

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
        assert "name" in response.json["columns"]
        assert "value" in response.json["columns"]

    def test_json_return_10_products(self):
        response = self.client.get("/api/product/")
        self.assertEqual(len(response.json['data']), 10)

    def test_json_return_product_factory(self):
        response = self.client.get("/api/product/")
        print(dir(response.json['columns']))
        index_name = response.json['columns'].index('name')
        for i in range(10):
            self.assertEqual(response.json['data'][i][index_name],
                    self.factory_products[i].name)




