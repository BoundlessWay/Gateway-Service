from fastapi import APIRouter

# Create a router instance
router = APIRouter()

# Define routes for event related endpoints
@router.get("/")
async def get_notification():
    return {"message": "List of payments"}

@router.get("/getPayment")
async def get_notification_details():
    return {"message": "Details of an payment"}

@router.post("/addPayment")
async def add_notification(event_data: dict):
    return {"message": "Payment added"}
