from fastapi import Depends, Request, HTTPException
from fastapi.templating import Jinja2Templates
from jwt_handler import get_current_user
from database import users_data
from fastapi import APIRouter
from cookie_handler import delete_access_token_cookie

router = APIRouter()
templates = Jinja2Templates(directory='templates')

@router.get('/users')
def users(request: Request, current_user: dict = Depends(get_current_user)):
    try:

        user_email = current_user.get("email")

        user = users_data.find_one({"email": user_email})

        username = user.get("username")

        role = user.get("role")

        if not user or user.get("role") != "admin":
            return templates.TemplateResponse('404.html', {'request': request})
        
        users_cursor = users_data.find()

        users = []

        for usr in users_cursor:
            users.append(usr)
        

        return templates.TemplateResponse("users.html", {
            "request": request,
            "users": users,
            "role": role,'username': username
        })
    
    except Exception as e:
        print(f"Error occurred in users get route: {e}")
        response = templates.TemplateResponse('login.html',{'request':request,'message':"please login to access this page"})
        delete_access_token_cookie(response)
        return response


@router.put('/users/{user_email}')
def edit_user(user_email: str, user_data: dict, current_user: dict = Depends(get_current_user)):
    try:

        current_user_email = current_user.get("email")

        user = users_data.find_one({"email": current_user_email})

        if not user or user.get("role") != "admin":
            raise HTTPException(status_code=401, detail="Unauthorized")
        
        result = users_data.update_one({"email": user_email}, {"$set": user_data})

        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="User not found")
        
        return {"message": "User updated successfully"}
    
    except Exception as e:
        print(f"Error occurred in users put route: {e}")
        response = templates.TemplateResponse('login.html')
        delete_access_token_cookie(response)
        return response



@router.delete('/users/{user_email}')
def delete_user(user_email: str, current_user: dict = Depends(get_current_user)):
    try:
        
        current_user_email = current_user.get("email")

        user = users_data.find_one({"email": current_user_email})

        if not user or user.get("role") != "admin":
            raise HTTPException(status_code=401, detail="Unauthorized")
        
        result = users_data.delete_one({"email": user_email})

        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="User not found")
        
        return {"message": "User deleted successfully"}
    
    except Exception as e:
        print(f"Error occurred in users delete route: {e}")
        response = templates.TemplateResponse('login.html')
        delete_access_token_cookie(response)
        return response