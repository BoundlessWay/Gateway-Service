from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
import httpx

router = APIRouter()

base_url = "https://account-service.boundlessway.id.vn"

@router.get("/users")
async def get_users():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{base_url}/users")
        if response.status_code == 200:
            return JSONResponse(content=response.json())
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch users")

@router.post("/login")
async def login(account_data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{base_url}/login", json=account_data)
        if response.status_code == 200:
            return JSONResponse(content=response.json())
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to login")

@router.post("/register/guest")
async def register_guest(account_data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{base_url}/register/guest", json=account_data)
        if response.status_code == 200:
            return JSONResponse(content=response.json())
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to register guest")

@router.post("/register/organization")
async def register_organization(account_data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{base_url}/register/organization", json=account_data)
        if response.status_code == 200:
            return JSONResponse(content=response.json())
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to register organization")
