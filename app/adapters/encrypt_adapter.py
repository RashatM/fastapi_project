from passlib.hash import bcrypt


class EncryptionAdapter:

    @staticmethod
    def get_password_hash(password: str) -> str:
        return bcrypt.hash(password)

    @staticmethod
    def verify_password(plain_password, hashed_password) -> bool:
        return bcrypt.verify(plain_password, hashed_password)