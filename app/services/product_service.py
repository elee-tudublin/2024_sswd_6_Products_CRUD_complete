from app.data_access.product_dba import dataGetProducts, dataGetProduct, dataAddProduct, dataUpdateProduct, dataDeleteProduct
from app.models.product import Product
import json

# get list of products from data
def getAllProducts() :
    products = dataGetProducts()
    return products

def getProduct(id) :
    return dataGetProduct(id)

# add new todo using data access
def newProduct(title: str, description: str, thumbnail: str, stock: int, price: float) :
    # add product (via dataaccess)
    print('price: ', price)
    input = Product(title=title, description=description, thumbnail=thumbnail, stock=stock, price=price)

    new_product = dataAddProduct(input)

    # return new product
    return new_product

# add new todo using data access
def updateProduct(id: int, title: str, description: str, thumbnail: str, stock: int, price: float) :
    # update product
    input = Product(id = id, title=title, description=description, thumbnail=thumbnail, stock=stock, price=price)

    product = dataUpdateProduct(input)

    # return updated product
    return product


def deleteProduct(id : int) :
    result = dataDeleteProduct(id)
