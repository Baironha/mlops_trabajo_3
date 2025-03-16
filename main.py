from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
import uuid

api = FastAPI(
    title="MLOPS first API",
    description="MLOPS first API",
    version="0.0.1",
)

@api.post("/users/", tags=["users"])
async def user_sing_up(data: dict):
    name = data["name"]
    username = data["username"]
    email = data["email"]


    return {
        "response": f"se ha creado exitosamente el usuario {username} con el email {email}",
        id: uuid.uuid4(),
        "name": name,
        "status_code":201
    }



@api.post("/products/", tags=["products"])
async def create_product(data: dict):
    product_name = data["product_name"]
    product_price = data["product_price"]

    try:
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "respuesta": "se ha creado exitosamente el producto",
                "id": uuid.uuid4(),
                "product_name": product_name,
                "product_price": product_price,
            }
        )
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@api.post("/create-password", tags=["Users"])
async def create_password(user: str, password: str):
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "id": str(uuid.uuid4()),
            "user": user,
            "password": password
        }
    )



@api.get("/get-users/{user_id}", tags=["users"])
async def get_user(user_id: str):
    user_data ={
        "78": {
            "email": "bhorna@fwdcostarica.com",
            "name": "Bairon"
        },
        "79": {
            "email": "fhorna@fwdcostarica.com",
            "name": "Fernando"
        }
    }
    try:
        user = user_data[user_id]
        if user is  not None:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content= user
            )
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "response": "no se encontro el usuario"
            }
        )
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
