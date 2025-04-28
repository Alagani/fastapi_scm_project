from fastapi import Request, Form, Depends, APIRouter
from fastapi.templating import Jinja2Templates
from database import users_data, shipment_data
from datetime import datetime
from .jwt_handler import get_current_user
from .cookie_handler import delete_access_token_cookie
from models import Shipment

router = APIRouter()

templates = Jinja2Templates(directory='templates')


@router.get('/new_shipment')
def create_shipment_get(request: Request, current_user: dict = Depends(get_current_user)):
    try:

        user_email = current_user['email']
        users = users_data.find_one({'email': user_email})
        role = users.get("role")
        username = users.get("username")
        today_date = datetime.now().strftime('%Y-%m-%d')
        return templates.TemplateResponse('new_shipment.html', {'request': request, 'role': role, 'today_date': today_date,'username': username})
    
    except Exception as e:
        print(f"Error in create_shipment_get route: {e}")
        response = templates.TemplateResponse('login.html',{'request':request,'message':"please login to access this page"})
        delete_access_token_cookie(response)
        return response


@router.post('/new_shipment')
def create_shipment_post(
    request: Request, current_user: dict = Depends(get_current_user),
    shipment_number: int = Form(...),
    route: str = Form(...),
    device_id: int = Form(...),
    po_number: int = Form(...),
    ndc_number: int = Form(...),
    goods_number: int = Form(...),
    container_number: int = Form(...),
    goods_type: str = Form(...),
    expected_delivery_date: str = Form(...),
    delivery_number: int = Form(...),
    batch_id: int = Form(...),
    shipment_description: str = Form(...)
):
    try:
        user_email = current_user['email']
        user = users_data.find_one({'email': user_email})
        role = user.get("role")
        username = user.get("username")

        if shipment_data.find_one({"shipment_number": shipment_number}):
            return templates.TemplateResponse(
                'new_shipment.html',
                {
                    'request': request,
                    'message': f"The shipment_number '{shipment_number}' already exists.",
                    'role': role
                }
            )

        elif shipment_data.find_one({"delivery_number": delivery_number}):
            return templates.TemplateResponse(
                'new_shipment.html',
                {
                    'request': request,
                    'message': f"The delivery_number '{delivery_number}' already exists.",
                    'role': role
                }
            )
        
        shipment_doc = Shipment(
            shipment_number=shipment_number,
            route=route,
            device_id=device_id,
            po_number=po_number,
            ndc_number=ndc_number,
            goods_number=goods_number,
            container_number=container_number,
            goods_type=goods_type,
            expected_delivery_date=expected_delivery_date,
            delivery_number=delivery_number,
            batch_id=batch_id,
            shipment_description=shipment_description,
            user_id=user_email,
            created_at=datetime.now()
        )

        result = shipment_data.insert_one(shipment_doc.dict())

        if not result.inserted_id:
            return templates.TemplateResponse(
                'new_shipment.html',
                {
                    'request': request,
                    'message': "Failed to create shipment. Please try again.",
                    'role': role 
                }
            )
        # Redirect to the same page with a success message
        return templates.TemplateResponse(
            'new_shipment.html',
            {
            'request': request,
            'success': "Shipment created successfully!",
            'username': username,
            'role': role
            }
        )
    except Exception as e:
        print(f"Error in create_shipment_post route: {e}")
        response = templates.TemplateResponse(
                'login.html',
                {
                    'request': request,
                    'message': "An error occurred while creating the shipment. Please login again."
                }
            )
        delete_access_token_cookie(response)
        return response