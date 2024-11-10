# import the model class
from app.models.product import Product
from starlette.config import Config
from supabase import create_client, Client



# Load environment variables from .env
config = Config(".env")

db_url: str = config("SUPABASE_URL")
db_key: str = config("SUPABASE_KEY")

supabase: Client = create_client(db_url, db_key)


# get all products
def dataGetProducts():
    response = supabase.table("product").select("*").execute()
    return response.data

# get product by id
def dataGetProduct(id):
    return True
