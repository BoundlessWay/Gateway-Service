from fastapi import FastAPI
from routes import account, event

app = FastAPI(docs_url="/")

app.include_router(account.router, prefix="/account")
app.include_router(event.router, prefix="/event")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
