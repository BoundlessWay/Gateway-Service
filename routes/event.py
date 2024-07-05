from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
import httpx

router = APIRouter()

event_base_url = "https://event-service-7nx8.onrender.com"

@router.get("/events")
async def get_all_events():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{event_base_url}/events")
        if response.status_code == 200:
            return JSONResponse(content=response.json())
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch events")

@router.get("/event/{event_id}")
async def get_event_by_id(event_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{event_base_url}/event/{event_id}")
        if response.status_code == 200:
            return JSONResponse(content=response.json())
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch event details")

@router.get("/event-type")
async def get_event_types():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{event_base_url}/event-type")
        if response.status_code == 200:
            return JSONResponse(content=response.json())
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch event types")

@router.post("/events")
async def create_event(event_data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{event_base_url}/events", json=event_data)
        if response.status_code == 200:
            return JSONResponse(content=response.json())
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to create event")
