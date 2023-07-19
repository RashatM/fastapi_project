from app.db.models.users import UserModel
from app.schemas.auth import UserPublicSchema, UserPrivateSchema


def convert_db_model_to_private_user_dto(user: UserModel) -> UserPrivateSchema:
    return UserPrivateSchema(
        id=user.id,
        email=user.email
    )


def convert_db_model_to_user_dto(user: UserModel) -> UserPublicSchema:
    return UserPublicSchema(
        id=user.id,
        email=user.email,
        hashed_password=user.hashed_password
    )
