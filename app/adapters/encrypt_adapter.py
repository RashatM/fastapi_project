from passlib.hash import bcrypt

from app.interfaces.adapters.encrypt_adapter import IEncryptionAdapter


class EncryptionAdapter(IEncryptionAdapter):

    @staticmethod
    def get_password_hash(password: str) -> str:
        return bcrypt.hash(password)

    @staticmethod
    def verify_password(plain_password, hashed_password) -> bool:
        return bcrypt.verify(plain_password, hashed_password)