from app.db.models.users import UserModel
from app.dto.auth import UserPublicDTO, UserPrivateDTO


def convert_db_model_to_private_user_dto(user: UserModel) -> UserPrivateDTO:
    return UserPrivateDTO(
        id=user.id,
        email=user.email
    )


def convert_db_model_to_user_dto(user: UserModel) -> UserPublicDTO:
    return UserPublicDTO(
        id=user.id,
        email=user.email,
        hashed_password=user.hashed_password
    )
