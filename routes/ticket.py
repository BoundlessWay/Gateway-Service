from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
import httpx

router = APIRouter()

ticket_base_url = "https://ticket-service.boundlessway.id.vn"

async def proxy_request(request: Request, url: str, method: str):
    async with httpx.AsyncClient(follow_redirects=True) as client:
        if method == 'GET':
            response = await client.get(url, headers=request.headers)
        elif method == 'POST':
            body = await request.json()
            response = await client.post(url, json=body, headers=request.headers)
        elif method == 'PUT':
            body = await request.json()
            response = await client.put(url, json=body, headers=request.headers)
        elif method == 'DELETE':
            response = await client.delete(url, headers=request.headers)
        else:
            raise HTTPException(status_code=405, detail="Method not allowed")

        if response.status_code in {200, 201, 204}:
            return JSONResponse(content=response.json())
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)

@router.get("/api/revenue")
async def get_total_revenue(request: Request):
    return await proxy_request(request, f"{ticket_base_url}/api/revenue", 'GET')

@router.get("/api/tickets-sold")
async def get_total_tickets_sold(request: Request):
    return await proxy_request(request, f"{ticket_base_url}/api/tickets-sold", 'GET')

@router.get("/api/tickets")
async def get_all_tickets(request: Request):
    return await proxy_request(request, f"{ticket_base_url}/api/tickets", 'GET')

@router.post("/api/tickets")
async def create_ticket(request: Request):
    return await proxy_request(request, f"{ticket_base_url}/api/tickets", 'POST')

@router.get("/api/tickets/{eventID}")
async def get_tickets_for_event(request: Request, eventID: str):
    return await proxy_request(request, f"{ticket_base_url}/api/tickets/{eventID}", 'GET')

@router.put("/api/tickets/{ticketID}")
async def update_ticket(request: Request, ticketID: str):
    return await proxy_request(request, f"{ticket_base_url}/api/tickets/{ticketID}", 'PUT')

@router.delete("/api/tickets/{ticketID}")
async def delete_ticket(request: Request, ticketID: str):
    return await proxy_request(request, f"{ticket_base_url}/api/tickets/{ticketID}", 'DELETE')

@router.post("/api/tickets/purchase")
async def purchase_ticket(request: Request):
    return await proxy_request(request, f"{ticket_base_url}/api/tickets/purchase", 'POST')

@router.post("/api/tickets/{ticketID}/cancel")
async def cancel_ticket(request: Request, ticketID: str):
    return await proxy_request(request, f"{ticket_base_url}/api/tickets/{ticketID}/cancel", 'POST')
