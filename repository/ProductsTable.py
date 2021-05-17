from typing import List
from models.Product import Product
from repository.Database import Database

class ProductsTable:

    #--------------------------------------------------------------
    def __init__(self):
        self.__database: Database = Database("root", "", "127.0.0.1", "hardware_solutions")
    
    #--------------------------------------------------------------
    def getProducts(self) -> List[Product]:
        self.__database.connect()
        products: List[Product] = []
        data = self.__database.getRecords("SELECT * from products")
        for row in data:
            product: Product = Product(row[0], row[1])
            product.setDescription(row[2])
            product.setCost(row[3])
            product.setPrice(row[4])
            product.setCategory(row[5])
            products.append(product)
        self.__database.close()
        return products

    #--------------------------------------------------------------
    def getProduct(self, id: int) -> Product:
        self.__database.connect()
        data = self.__database.getRecord(f'SELECT * from products where product_id={id}')
        product: Product = Product(data[0], data[1])
        product.setDescription(data[2])
        product.setCost(data[3])
        product.setPrice(data[4])
        product.setCategory(data[5])
        self.__database.close()
        return product