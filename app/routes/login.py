from fastapi import Request,Form
from fastapi.templating import Jinja2Templates
from app.database import users_data
from app.cookie_handler import set_access_token_cookie
from fastapi.responses import RedirectResponse
# from passlib.context import CryptContext
from app.routes.register import verify_password
from fastapi import APIRouter
from app.jwt_handler import create_access_token

router = APIRouter()
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
templates = Jinja2Templates(directory='app/templates')

# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)


@router.get("/login")
def login(request:Request):
    return templates.TemplateResponse("login.html", {
        "request": request
    })
            

@router.post("/login")
def submit_login(
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
                "message": "User doesn't exist."
            })

        # --- Verify password ---
        if not verify_password(password, user["password"]):
            return templates.TemplateResponse("login.html", {
                "request": request,
                "message": "Incorrect Password."
            })

        access_token = create_access_token(
        data={"sub": user["email"]}
    )

        response = RedirectResponse(url="/dashboard", status_code=302)

        set_access_token_cookie(response, access_token)


        return response

    except Exception as e:
        print("error:", e)
        return templates.TemplateResponse("login.html", {
        "request": request,
        "message": "An unexpected error occurred. Please try again later."
})
    
