from fastapi import FastAPI
from sqlalchemy.ext.asyncio import async_sessionmaker

from app.adapters.encrypt_adapter import EncryptionAdapter
from app.dependencies.users import user_repository_provider, uow_provider, provide_uow, provide_user_repository, \
    auth_provider, session_provider, encrypt_provider
from app.providers.auth_provider import AuthenticationProvider
from app.providers.db_provider import DBProvider


def setup_di(app: FastAPI, pool: async_sessionmaker) -> None:
    db_provider = DBProvider(pool)

    app.dependency_overrides[session_provider] = db_provider.provide_session
    app.dependency_overrides[auth_provider] = AuthenticationProvider
    app.dependency_overrides[encrypt_provider] = EncryptionAdapter
    app.dependency_overrides[uow_provider] = provide_uow
    app.dependency_overrides[user_repository_provider] = provide_user_repository

