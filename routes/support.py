from fastapi import APIRouter

# Create a router instance
router = APIRouter()

# Define routes for event related endpoints
@router.get("/")
async def get_support():
    return {"message": "List of supports"}

@router.get("/getSupport")
async def get_support_details():
    return {"message": "Details of an support"}

@router.post("/addSupport")
async def add_support(event_data: dict):
    return {"message": "Support added"}
