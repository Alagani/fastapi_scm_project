from fastapi import Request,Form
from fastapi.templating import Jinja2Templates
from app.database import users_data
from fastapi import APIRouter
from passlib.context import CryptContext
import re
from app.models import Users

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
templates = Jinja2Templates(directory='app/templates')


def get_hashed_password(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

@router.get('/')
def landing_page(request:Request):
    return templates.TemplateResponse('landing_page.html',{'request':request})

@router.get('/register')
def register(request:Request):
    return templates.TemplateResponse('register.html',{'request':request})



@router.post("/register")
def register_user(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    confirm_password: str = Form(...)
):
    
    try:
        # --- Password match check ---
        if password != confirm_password:
            return templates.TemplateResponse("register.html", {
                "request": request,
                "message": "Passwords do not match."
            })


        if len(password) < 8:
            return templates.TemplateResponse("register.html", {
            "request": request,
            "message": "Password should be at least 8 characters long"
        })


        if not any(char.isdigit() for char in password):
            return templates.TemplateResponse("register.html", {
                "request": request,
                "message": "Password should contain at least one digit"
            })
        
        
        if not any(char.isalpha() for char in password):
            return templates.TemplateResponse("register.html", {
            "request":request,
            "message":"Password should contain at least one alphabets"
            })
        
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            return templates.TemplateResponse("register.html", {
                "request": request,
                "message": "Password should contain at least one special character"
            })
        
       
        # --- Email existence check ---
        if users_data.find_one({"email": email}):
            return templates.TemplateResponse("register.html", {
                "request": request,
                "message": "Email already registered."
            })



        # --- Save user with hashed password ---
        hashed_password = pwd_context.hash(password)
        
        user_doc = Users(
        username=username,
        email=email,
        password=hashed_password
        )


        users_data.insert_one(user_doc.model_dump())


        return templates.TemplateResponse("login.html", {
            "request": request,
            "success": "Registered Successful."
        })


    except Exception as e:
        return templates.TemplateResponse("register.html", {
            "request": request,
            "message": "Something went wrong. Please try again."
        })