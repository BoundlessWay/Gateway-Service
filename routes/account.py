from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_account():
    return {"message": "This is the /account endpoint"}

@router.get("/getAccount")
async def get_account_details():
    return {"message": "This is the /account/getAccount endpoint"}

@router.post("/addAccount")
async def add_account():
    return {"message": "This is the /account/addAccount endpoint"}
