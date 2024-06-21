from fastapi import FastAPI
from routes import account, event

app = FastAPI()

# Include routers from account and event modules
app.include_router(account.router, prefix="/account")
app.include_router(event.router, prefix="/event")

if __name__ == "__main__":
    import uvicorn

    # Run FastAPI application using Uvicorn server
    uvicorn.run("app:app", host="localhost", port=8000, reload=True)
