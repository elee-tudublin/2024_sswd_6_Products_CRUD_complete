from fastapi import Request
from app.data_access.product_dba import dataGetProducts, dataGetProduct
from app.models.product import Product
import json

# get list of products from data
def getAllProducts() :
    products = dataGetProducts()
    return products

def getProduct(id) :
    return dataGetProduct(id)