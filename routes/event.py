from fastapi import APIRouter

# Create a router instance
router = APIRouter()

# Define routes for event related endpoints
@router.get("/")
async def get_events():
    return {"message": "List of events"}

@router.get("/getEvent")
async def get_event_details():
    return {"message": "Details of an event"}

@router.post("/addEvent")
async def add_event(event_data: dict):
    return {"message": "Event added"}
