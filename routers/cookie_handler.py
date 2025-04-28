from fastapi.responses import Response

def set_access_token_cookie(response: Response, access_token: str):
    response.set_cookie(
        key="access_token",
        value=f"Bearer {access_token}",
        httponly=True,
        secure=False,
        max_age=60 * 100
    )

def delete_access_token_cookie(response: Response):
    response.delete_cookie(key="access_token")