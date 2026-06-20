from fastapi import APIRouter, Depends, Request

from app.middleware.auth_middleware import get_current_user

from app.schemas.product_schema import ProductResponse

from app.services.product_service import fetch_products

router = APIRouter(tags=["Products"])


@router.get("/products", response_model=list[ProductResponse], summary="View Products", description="""
            Retrieve products from Inventory Service.

            Features:

            - Product ID
            - Product Name
            - SKU
            - Product Price

            Data is retrieved from Project 4.""")

def get_products(request: Request, current_user=Depends(get_current_user)):

    authorization_header = request.headers.get("Authorization")

    token = authorization_header.replace("Bearer ", "")

    return fetch_products(token)