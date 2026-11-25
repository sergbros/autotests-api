#from clients.authentication.authentication_schema import TokenSchema

#print(TokenSchema.model_json_schema())

import jsonschema

from api_client_get_user import private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import get_random_email

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)
create_user_response = public_users_client.create_user_api(create_user_request)
# Получаем JSON-схему из Pydantic-модели ответа
create_user_response_schema = CreateUserResponseSchema.model_json_schema()

create_user_response_json = create_user_response.json()

create_user_response_schema = CreateUserResponseSchema.model_json_schema()

create_user_response_json = create_user_response.json()
#del create_user_response_json['user']['email']  #намеренно портим JSON удалением поля

# Проверяем, что JSON-ответ от API соответствует ожидаемой JSON-схеме
jsonschema.validate(instance=create_user_response.json(), schema=create_user_response_schema)
#jsonschema.validate(instance=create_user_response_json, schema=create_user_response_schema)     # валидация не проходит

# print(create_user_response.json())
# print(create_user_response_schema)

#create_user_response_json['user']['email'] = "hello!"   #намеренно портим JSON записью простого текста в Email

validate_json_schema(instance=create_user_response_json, schema=create_user_response_schema)