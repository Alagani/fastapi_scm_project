from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi.responses import RedirectResponse
from fastapi import Cookie, HTTPException
import os
from dotenv import load_dotenv
load_dotenv()



JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM =os.getenv("JWT_ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES=os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")


def create_access_token(data: dict, expires_delta: int = 15):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=expires_delta)
    to_encode.update({'exp':expire})
    return jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)


def get_current_user(access_token: str = Cookie(None)):
    if not access_token:
        return RedirectResponse(url="/login")
    
    try:
        token = access_token.replace("Bearer ", "")
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=403, detail="Invalid token payload")
        return {"email": email}
    
    except JWTError:
        return RedirectResponse(url="/login")