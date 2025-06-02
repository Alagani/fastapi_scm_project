from fastapi.responses import Response

def set_access_token_cookie(response: Response, access_token: str):
    response.set_cookie(

        key="access_token",
        value=f"Bearer {access_token}",
        httponly=True,      # Block JS access to cookie (helps prevent XSS)
        max_age=60*10,      # expires after 10 minutes (600 seconds)
        samesite="Strict",  # protecting against CSRF attacks
        secure=False        # Allow HTTP (not HTTPS only)

    )

def delete_access_token_cookie(response: Response):
    response.delete_cookie(key="access_token")