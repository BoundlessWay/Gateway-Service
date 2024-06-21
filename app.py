from fastapi import FastAPI
from routes import account, event

app = FastAPI(docs_url="/")

# Include routers from account and event modules
app.include_router(account.router, prefix="/account", tags=["Account"])
app.include_router(event.router, prefix="/event", tags=["Event"])

if __name__ == "__main__":
    import uvicorn

    # Run FastAPI application using Uvicorn server
    uvicorn.run("app:app", host="localhost", port=8000, reload=True)
