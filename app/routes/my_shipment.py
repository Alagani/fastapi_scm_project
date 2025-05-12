from fastapi import Request, Depends, APIRouter
from fastapi.templating import Jinja2Templates
from database import users_data, shipment_data
from jwt_handler import get_current_user
from cookie_handler import delete_access_token_cookie

router = APIRouter()
templates = Jinja2Templates(directory='templates')


@router.get('/my_shipment')
def my_shipment(request: Request, current_user: dict = Depends(get_current_user)):
    try:
        user_email = current_user["email"]
        user = users_data.find_one({"email": user_email})
        username= user.get("username")
        role = user.get("role")
        if user.get("role") == "admin":
            shipments_cursor = shipment_data.find()
        else:
            shipments_cursor = shipment_data.find({"user_id": user_email})
        
        shipments = []
        for doc in shipments_cursor:
            shipments.append(doc)
        
        return templates.TemplateResponse('my_shipment.html', {
            'request': request,
            'shipments': shipments,
            'role': role,
            'username': username
        })

    except Exception as e:
        print(f"Error fetching shipments: {str(e)}")
        response = templates.TemplateResponse('login.html',{'request':request,'message':"please login to access this page"})
        delete_access_token_cookie(response)
        return response