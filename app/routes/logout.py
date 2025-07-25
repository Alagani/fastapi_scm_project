from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Request
from app.cookie_handler import delete_access_token_cookie

router = APIRouter()
templates = Jinja2Templates(directory='app/templates')


@router.get('/logout')
def logout(request: Request):
    response = templates.TemplateResponse(
        'login.html',
        {'request':request,
            'message': 'You have been logged out successfully.'
        }
    )
    delete_access_token_cookie(response)
    return response