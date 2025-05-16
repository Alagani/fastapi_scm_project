from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates
from app.jwt_handler import get_current_user
from app.database import device_data,users_data
from fastapi import APIRouter
from app.cookie_handler import delete_access_token_cookie

router = APIRouter()

templates = Jinja2Templates(directory='app/templates')

@router.get('/devicedata')
def devicedata(request:Request,current_user: dict = Depends(get_current_user)):
    try:

        user_email = current_user["email"]

        user = users_data.find_one({'email':user_email})
        
        username= user.get("username")

        role = user.get("role")

        if role != "admin":
            return templates.TemplateResponse('page_not_found.html', {'request': request})
        else:
            devices_cursor = device_data.find()

        devices = []

        for device in devices_cursor:
            devices.append(device)
            
        return templates.TemplateResponse('device_data.html',{'request':request,"role":role,'devices':devices,'username': username})
    
    except Exception as e:
        print(f"Error in devicedata route: {e}")
        response = templates.TemplateResponse('login.html',{'request':request,'message':"please login to access this page"})
        delete_access_token_cookie(response)
        return response
    