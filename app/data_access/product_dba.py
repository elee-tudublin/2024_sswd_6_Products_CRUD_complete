# import the model class
from app.models.product import Product
from starlette.config import Config
import httpx


# Load environment variables from .env
config = Config(".env")

# A dictionary for products
products_data = {}

# initialise with data from dummyjson
def dataInitDB() :

    # use global var
    global products_data

    # data already exists
    if (products_data) :
        return True

    # Get data
    response = httpx.get(config("PRODUCT_DATA_URL"))
    data = response.json()
    products_data = data['products']

    #print("data initialised: ", products_data)
    return True

# get all products
def dataGetProducts():
    global products_data
    # force init if first time
    check_data: bool = dataInitDB()
    return products_data

# get product by id
def dataGetProduct(id):
    return products_data[id]
