from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi import Depends
from jwt_handler import get_current_user
from database import users_data
from fastapi import APIRouter
from cookie_handler import delete_access_token_cookie

router = APIRouter()

templates = Jinja2Templates(directory='templates')

@router.get('/dashboard')
def dashboard(request:Request,current_user: dict = Depends(get_current_user)):
    try:

        user_email = current_user['email']

        user = users_data.find_one({"email":user_email})

        username = user.get("username")
        role =user.get("role")

        return templates.TemplateResponse('dashboard.html',{'request':request,"current_user":current_user,'role':role,'username':username})
    
    except Exception as e:
        print(f"Error in dashboard route: {e}")
        response = templates.TemplateResponse('login.html',{'request':request,'message':"please login to access this page"})
        delete_access_token_cookie(response)
        return response
    