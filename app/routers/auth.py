from fastapi import APIRouter, Depends, Response, status
from pydantic import EmailStr

from app.dependencies.users import get_auth_service, get_current_user
from app.exceptions.auth_exceptions import UserAlreadyExistsException
from app.exceptions.error_handlers.error_result import ErrorResult
from app.interfaces.services.auth import IAuthenticationService
from app.dto.auth import TokenDTO, UserPrivateDTO

auth_router = APIRouter(
    prefix="/auth",
    tags=["Аутентификация и Авторизация"]
)


@auth_router.post(
    "/register",
    responses={
        status.HTTP_409_CONFLICT: {
            "model": ErrorResult[UserAlreadyExistsException]
        }
    },
    status_code=status.HTTP_201_CREATED)
async def register_user(
    email: EmailStr,
    password: str,
    service: IAuthenticationService = Depends(get_auth_service)
) -> UserPrivateDTO:
    return await service.register_new_user(email=email, password=password)


@auth_router.post("/login")
async def login_user(
    response: Response,
    email: EmailStr,
    password: str,
    service: IAuthenticationService = Depends(get_auth_service)
) -> TokenDTO:
    token = await service.login_user(email, password)
    response.set_cookie("booking_access_token", token.access_token, httponly=True)
    return token


@auth_router.post("/logout")
async def logout(response: Response):
    response.delete_cookie("booking_access_token")


@auth_router.get("/me")
async def read_user_me(current_user: UserPrivateDTO = Depends(get_current_user)) -> UserPrivateDTO:
    return current_user





















