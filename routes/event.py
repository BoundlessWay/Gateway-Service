from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_event():
    return {"message": "This is the /event endpoint"}

@router.get("/getEvent")
async def get_event_details():
    return {"message": "This is the /event/getEvent endpoint"}

@router.post("/addEvent")
async def add_event():
    return {"message": "This is the /event/addEvent endpoint"}
