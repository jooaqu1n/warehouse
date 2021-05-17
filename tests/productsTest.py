from models.Product import Product
from typing import List
from repository.ProductsTable import ProductsTable

def test():
    table: ProductsTable = ProductsTable()
    products: List[Product] = table.getProducts()
    print(products[0])
    print(products[1])
    print(products[2])

    product: Product = table.getProduct(1)
    print(product)