from fastapi import APIRouter

# Create a router instance
router = APIRouter()

# Define routes for event related endpoints
@router.get("/")
async def get_tickets():
    return {"message": "List of tickets"}

@router.get("/getTicket")
async def get_event_details():
    return {"message": "Details of an ticket"}

@router.post("/addTicket")
async def add_event(event_data: dict):
    return {"message": "Ticket added"}
