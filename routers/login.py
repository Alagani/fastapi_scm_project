from fastapi import Request,Form
from fastapi.templating import Jinja2Templates
from database import users_data
from .cookie_handler import set_access_token_cookie
from fastapi.responses import RedirectResponse
from passlib.context import CryptContext
from fastapi import APIRouter
from .jwt_handler import create_access_token

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
templates = Jinja2Templates(directory='templates')

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)




@router.get("/login")
def login(request:Request):
    return templates.TemplateResponse("login.html", {
        "request": request
    })
            

@router.post("/login")
def login_post(
    request: Request,
    email: str = Form(...),
    password: str = Form(...)
):
    try:
        # --- Fetch user from DB ---
        user = users_data.find_one({"email": email})
        if not user:
            return templates.TemplateResponse("login.html", {
                "request": request,
                "message": "Invalid email or password."
            })

        # --- Verify password ---
        if not verify_password(password, user["password"]):
            return templates.TemplateResponse("login.html", {
                "request": request,
                "message": "Invalid email or password."
            })

        access_token = create_access_token(
        data={"sub": user["email"]}
    )

        response = RedirectResponse(url="/dashboard", status_code=302)

        set_access_token_cookie(response, access_token)


        return response

    except Exception as e:
        print("error:", str(e))
        return templates.TemplateResponse("login.html", {
        "request": request,
        "message": "An unexpected error occurred. Please try again later."
})
    
