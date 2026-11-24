from fastapi import FastAPI
from fastapi import FastAPI, status, HTTPException

app = FastAPI()


@app.get("/")
def home():
    return {"message": "QA Automation API is running"}

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

products = {}
next_id = 1


class ProductCreate(BaseModel):
    name: str
    price: int


@app.get("/")
def home():
    return {"message": "QA Automation API is running"}


@app.post("/products", status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate):
    global next_id

    new_product = {
        "id": next_id,
        "name": product.name,
        "price": product.price
    }

    products[next_id] = new_product
    next_id += 1

    return new_product

@app.get("/products/{product_id}")
def get_product(product_id: int):
    if product_id not in products:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return products[product_id]

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    if product_id not in products:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    del products[product_id]

    return {"message": "Product deleted"}

@app.put("/products/{product_id}")
def update_product(product_id: int, product: ProductCreate):
    if product_id not in products:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    updated_product = {
        "id": product_id,
        "name": product.name,
        "price": product.price
    }

    products[product_id] = updated_product

    return updated_product

