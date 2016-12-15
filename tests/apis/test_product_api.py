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
        print(response)
        self.assertEqual(len(response.json['data']), 10)

    def test_json_return_product_factory(self):
        response = self.client.get("/api/product/")
        index_id = response.json['columns'].index('id')
        index_name = response.json['columns'].index('name')
        index_value = response.json['columns'].index('value')
        for i in range(10):
            self.assertEqual(response.json['data'][i][index_id],
                    self.factory_products[i].id)
            self.assertEqual(response.json['data'][i][index_name],
                    self.factory_products[i].name)
            self.assertEqual(response.json['data'][i][index_value],
                    self.factory_products[i].value)


    def test_json_shoudl_return_not_repeated_products(self):
        response = self.client.get("/api/product/")
        index_name = response.json['columns'].index('name')
        list_data = [row[index_name] for row in response.json['data']]
        self.assertEqual(len(list_data), len(set(list_data)))
        










































