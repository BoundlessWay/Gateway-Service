from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
import httpx

router = APIRouter()

event_base_url = "https://event-service-7nx8.onrender.com"

async def proxy_request(request: Request, url: str, method: str):
    async with httpx.AsyncClient(follow_redirects=True) as client:
        if method == 'GET':
            response = await client.get(url)
        elif method == 'POST':
            body = await request.json()
            response = await client.post(url, json=body)
        elif method == 'PUT':
            body = await request.json()
            response = await client.put(url, json=body)
        elif method == 'DELETE':
            response = await client.delete(url)
        elif method == 'PATCH':
            body = await request.json()
            response = await client.patch(url, json=body)
        else:
            raise HTTPException(status_code=405, detail="Method not allowed")

        if response.status_code in {200, 201}:
            return JSONResponse(content=response.json())
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)

@router.get("/events")
async def get_all_events(request: Request):
    return await proxy_request(request, f"{event_base_url}/events", 'GET')

@router.get("/event/{event_id}")
async def get_event_by_id(request: Request, event_id: str):
    return await proxy_request(request, f"{event_base_url}/event/{event_id}", 'GET')

@router.get("/event-type")
async def get_event_types(request: Request):
    return await proxy_request(request, f"{event_base_url}/event-type", 'GET')

@router.post("/events")
async def create_event(request: Request):
    return await proxy_request(request, f"{event_base_url}/events", 'POST')

@router.put("/event/{event_id}")
async def update_event(request: Request, event_id: str):
    return await proxy_request(request, f"{event_base_url}/event/{event_id}", 'PUT')

@router.delete("/event/{event_id}")
async def delete_event(request: Request, event_id: str):
    return await proxy_request(request, f"{event_base_url}/event/{event_id}", 'DELETE')
