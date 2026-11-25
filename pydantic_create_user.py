from pydantic import BaseModel, EmailStr, Field, PositiveInt


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName", gt=3)


class CreateUserRequestDict(BaseModel):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName", gt=3)


class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя.
    """
    user: UserSchema
