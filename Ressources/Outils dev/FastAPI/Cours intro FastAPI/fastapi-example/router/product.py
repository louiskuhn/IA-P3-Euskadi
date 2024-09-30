from typing import Optional, List
from fastapi import APIRouter, Header, Cookie, Form
from fastapi.responses import Response, HTMLResponse, PlainTextResponse
import time

router = APIRouter(
  prefix='/product',
  tags=['product']
)

products = ['watch', 'camera', 'phone']
prices = [10, 100, 50]

async def slow_function():
  time.sleep(7)
  return "done"

@router.post('/new')
def create_product(name: str = Form(...), price: int = Form(...)):
  products.append(name)
  prices.append(price)
  return {products[k]: prices[k] for k in range(len(products))}


@router.get('/all')
async def get_all_products():
  await slow_function()
  data = " ".join(products)
  response = Response(content=data, media_type="text/plain")
  response.set_cookie(key="test_cookie", value="test_cookie_value")
  return response

@router.get('/all/prices')
def get_all_products():
  return prices

@router.get('/withheader')
def get_products(
  response: Response,
  custom_header: Optional[List[str]] = Header(None),
  test_cookie: Optional[str] = Cookie(None)
  ):
  if custom_header:
    response.headers['custom_response_header'] = " and ".join(custom_header)
  return {
    'data': products,
    'custom_header': custom_header,
    'my_cookie': test_cookie
  }


@router.get('/{id}', responses={
  200: {
    "content": {
      "text/html": {
        "example": "<div>Product</div>"
      }
    },
    "description": "Returns the HTML for an object"
  },
  404: {
    "content": {
      "text/plain": {
        "example": "Product not available"
      }
    },
    "description": "A cleartext error message"
  }
})
def get_product(id: int):
  if id > len(products):
    out = "Product not available"
    return PlainTextResponse(status_code=404, content=out, media_type="text/plain")
  else:
    product = products[id]
    out = f"""
    <head>
      <style>
      .product {{
        width: 500px;
        height: 30px;
        border: 2px inset green;
        background-color: lightblue;
        text-align: center;
      }}
      </style>
    </head>
    <div class="product">{product}</div>
    """
    return HTMLResponse(content=out, media_type="text/html")