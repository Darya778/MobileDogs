from fastapi import FastAPI
from users.router import router as user_router
from devices.router import router as device_router
from tasks.router import router as device_router

app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(device_router, prefix="/device", tags=["devices"])
app.include_router(device_router, prefix="/tasks", tags=["devices"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the IoT Project API"}
