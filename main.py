from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

USER_SERVICE_URL = 'https://logging-service-production.up.railway.app/user'
EVENT_SERVICE_URL = 'https://logging-service-production.up.railway.app/system'

@app.get("/account")
async def get_account():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(USER_SERVICE_URL)
            response.raise_for_status()  # Kiểm tra lỗi HTTP

        content_type = response.headers.get('Content-Type', '')

        if 'application/json' in content_type:
            return response.json()
        elif 'text/html' in content_type:
            return {"html_content": response.text}
        else:
            raise HTTPException(status_code=500, detail="Unexpected content type received")

    except httpx.HTTPStatusError as exc:
        # Trả về lỗi chi tiết nếu có lỗi HTTP
        raise HTTPException(status_code=exc.response.status_code, detail=str(exc))
    except Exception as exc:
        # Trả về lỗi chung nếu có lỗi khác
        raise HTTPException(status_code=500, detail=str(exc))
    
@app.get("/account/getAccount")
async def get_account_details():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{USER_SERVICE_URL}/account/getAccount")
    return response.json()

@app.post("/account/addAccount")
async def add_account(account_data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{USER_SERVICE_URL}/account/addAccount", json=account_data)
    return response.json()

@app.get("/event")
async def get_event():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{EVENT_SERVICE_URL}")
    return response.json()

@app.get("/event/getEvent")
async def get_event_details():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{EVENT_SERVICE_URL}/event/getEvent")
    return response.json()

@app.post("/event/addEvent")
async def add_event(event_data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{EVENT_SERVICE_URL}/event/addEvent", json=event_data)
    return response.json()
