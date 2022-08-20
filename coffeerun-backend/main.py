from typing import Optional
from fastapi import FastAPI, Form, HTTPException
from urllib.parse import unquote
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

databases = []


@app.post("/")
def create_coffee_order(emailAddress: str = Form(), coffee: str = Form(), size: Optional[str] = Form(''), flavor: Optional[str] = Form(''), strength: Optional[int] = Form(0)):
    for coffee in databases:
        if coffee["emailAddress"] == emailAddress:
            raise HTTPException(
                status_code=422, detail="Resource already exist")
    coffee = {"emailAddress": emailAddress,
              "coffee": coffee, "size": size, "flavor": flavor}
    databases.append(coffee)
    return coffee


@app.get("/")
def get_coffee_orders():
    return databases


@app.delete("/{email}")
def delete_coffer_orders(email: str):
    index = 0
    while index < len(databases):
        coffer = databases[index]
        if coffer["emailAddress"] == unquote(email):
            databases.remove(coffer)
            return {}
        index = index + 1
    raise HTTPException(
        status_code=404, detail="Resource not found")


@app.get("/{email}")
def get_item(email: str):
    for coffee in databases:
        if coffee["emailAddress"] == unquote(email):
            return coffee
    raise HTTPException(
        status_code=404, detail="Resource not found")
