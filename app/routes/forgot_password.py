from fastapi import Request,Form
from fastapi.templating import Jinja2Templates
from app.database import users_data
# from passlib.context import CryptContext
from app.routes.register import get_hashed_password
from fastapi import APIRouter
import re

router = APIRouter()
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
templates = Jinja2Templates(directory='app/templates')


@router.get("/forget_password")
def password_reset_form(request: Request):
    return templates.TemplateResponse("forget_password.html", {
        "request": request,
        "step": "email_form"  # Initial step
    })




@router.post("/forget_password")
def handle_password_reset(
    request: Request,
    email: str = Form(...),
    password: str = Form(None),
    confirm_password: str = Form(None)  
):
    try:
    # Step 1: Email submission
        if email and not password:
            user = users_data.find_one({"email": email})
            if not user:
                return templates.TemplateResponse("forget_password.html", {
                    "request": request,
                    "step": "email_form",
                    "message": "No account found with that email."
                })
            
            return templates.TemplateResponse("forget_password.html", {
                "request": request,
                "step": "reset_form",
                "email": email
            })
        
        # Step 2: Password reset submission
        if email and password and confirm_password:
            # First check password match
            if password != confirm_password:
                return templates.TemplateResponse("forget_password.html", {
                    "request": request,
                    "step": "reset_form",
                    "email": email,
                    "message": "Passwords don't match."
                })
            
            # Validate password strength
            error_message = None
            
            if len(password) < 8:
                error_message = "Password must be at least 8 characters long"
            elif not re.search(r'\d', password):  # Check for at least one digit
                error_message = "Password must contain at least one number (0-9)"
            elif not re.search(r'[a-zA-Z]', password):  # Check for at least one letter
                error_message = "Password must contain at least one letter"
            elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):  # Check for special char
                error_message = "Password must contain at least one special character"
            
            if error_message:
                return templates.TemplateResponse("forget_password.html", {
                    "request": request,
                    "step": "reset_form",
                    "email": email,
                    "message": error_message
                })
            
        
            
            # Update password in database
            hashed_password = get_hashed_password(password)
            users_data.update_one(
                {"email": email},
                {"$set": {"password": hashed_password}}
            )

            return templates.TemplateResponse("login.html", {
                    "request": request,
                    "success": "Password changed successfully."
                })



    except Exception as e:
        print(f"Error in forgot_password route: {e}")
        response = templates.TemplateResponse(
            'login.html',
            {
                'request': request,
                'message': "try again."
            }
        )
        return response
