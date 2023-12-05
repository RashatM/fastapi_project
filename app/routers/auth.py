from fastapi import APIRouter, Depends, Response, status


from app.dependencies.users import get_auth_service, get_current_user
from app.exceptions.auth_exceptions import UserAlreadyExistsException
from app.exceptions.error_handlers.error_result import ErrorResult
from app.services.auth import AuthenticationService
from app.schemas.auth import UserRequestSchema, UserPublicSchema, Token, UserPrivateSchema, UserRequestSchema

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
    user_data: UserRequestSchema,
    service: AuthenticationService = Depends(get_auth_service)
) -> UserPrivateSchema:
    return await service.register_new_user(email=user_data.email, password=user_data.password)


@auth_router.post("/login")
async def login_user(
    response: Response,
    user_data: UserRequestSchema,
    service: AuthenticationService = Depends(get_auth_service)
) -> Token:
    token = await service.login_user(user_data.email, user_data.password)
    response.set_cookie("booking_access_token", token.access_token, httponly=True)
    return token


@auth_router.post("/logout")
async def logout(response: Response):
    response.delete_cookie("booking_access_token")


@auth_router.get("/me")
async def read_user_me(current_user: UserPrivateSchema = Depends(get_current_user)) -> UserPrivateSchema:
    return current_user





















