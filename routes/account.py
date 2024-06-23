from fastapi import APIRouter, Request, HTTPException

# Create a router instance
router = APIRouter()

# Define routes for account related endpoints
@router.get("/")
async def get_accounts():
    return {"message": "List of accounts"}

@router.get("/getAccount")
async def get_account_details():
    return {"message": "Details of an account"}

@router.post("/addAccount")
async def add_account(account_data: dict):
    return {"message": "Account added"}
