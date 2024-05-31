from fastapi import FastAPI
from .users import router as user_router
from .devices import router as device_router

app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(device_router, prefix="/devices", tags=["devices"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the IoT Project API"}
