from pydantic import BaseModel, Field

from tools.fakers import fake


# Добавили суффикс Schema вместо Dict
class TokenSchema(BaseModel):  # Наследуем от BaseModel вместо TypedDict
    """
    Описание структуры аутентификационных токенов.
    """
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")


# Добавили суффикс Schema вместо Dict
class LoginRequestSchema(BaseModel):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)


# Добавили суффикс Schema вместо Dict
class LoginResponseSchema(BaseModel):  # Наследуем от BaseModel вместо TypedDict
    """
    Описание структуры ответа аутентификации.
    """
    token: TokenSchema


# Добавили суффикс Schema вместо Dict
class RefreshRequestSchema(BaseModel):  # Наследуем от BaseModel вместо TypedDict
    """
    Описание структуры запроса для обновления токена.
    """
    refresh_token: str = Field(alias="refreshToken", default_factory=fake.sentence)


print(LoginRequestSchema())
print(LoginRequestSchema(email='mail@mail.mail', password='1qaz2WSX'))
print(LoginRequestSchema())
