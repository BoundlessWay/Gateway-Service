from fastapi import APIRouter

# Create a router instance
router = APIRouter()

# Define routes for event related endpoints
@router.get("/")
async def get_notification():
    return {"message": "List of notifications"}

@router.get("/getNotification")
async def get_event_details():
    return {"message": "Details of an notification"}

@router.post("/addNotification")
async def add_event(event_data: dict):
    return {"message": "Notification added"}
