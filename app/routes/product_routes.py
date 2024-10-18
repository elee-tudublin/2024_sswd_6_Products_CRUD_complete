from typing import Annotated
from fastapi import APIRouter, Form
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# import service functions
from app.services.product_service import getAllProducts, getProduct

from app.models.product import Product

router = APIRouter()

# set location for templates
templates = Jinja2Templates(directory="app/view_templates")

# handle http get requests for the site root /
# return the todos page
@router.get("/", response_class=HTMLResponse)
async def todos(request: Request):

    products = getAllProducts()

    # note passing of parameters to the page
    return templates.TemplateResponse("product/products.html", {"request": request, "products": products })
