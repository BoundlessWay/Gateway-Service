from fastapi import FastAPI
from routes import account, event, notification, payment, support, ticket
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(docs_url="/")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers from account and event modules
app.include_router(account.router, prefix="/account", tags=["Account"])
app.include_router(event.router, prefix="/event", tags=["Event"])
app.include_router(ticket.router, prefix="/ticket", tags=["Ticket and Report"])
app.include_router(payment.router, prefix="/payment", tags=["Payment"])
app.include_router(notification.router, prefix="/notification", tags=["Notification and Promotion"])
app.include_router(support.router, prefix="/support", tags=["Customer Support"])


    
