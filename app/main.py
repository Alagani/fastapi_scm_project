from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import login,register, device_data, new_shipment, dashboard, users, my_shipment,logout
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory='app/templates')

# Included routers
app.include_router(login.router)
app.include_router(register.router)
app.include_router(users.router)
app.include_router(device_data.router)
app.include_router(dashboard.router)
app.include_router(new_shipment.router)
app.include_router(my_shipment.router)
app.include_router(logout.router)