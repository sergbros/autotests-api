"""
{
  "course": {
    "id": "string",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "description": "string",
    "previewFile": {
      "id": "string",
      "filename": "string",
      "directory": "string",
      "url": "https://example.com/"
    },
    "estimatedTime": "string",
    "createdByUser": {
      "id": "string",
      "email": "user@example.com",
      "lastName": "string",
      "firstName": "string",
      "middleName": "string"
    }
  }
}
"""
import uuid

from pydantic import BaseModel, Field, ConfigDict, computed_field, HttpUrl, EmailStr, ValidationError, FilePath, IPv4Address
from pydantic.alias_generators import to_camel


class FileSchema(BaseModel):
    id: str
    url: HttpUrl
    filename: str
    directory: str


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName", gt=1)

    @computed_field
    def username(self) -> str:
        return f"{self.last_name} {self.first_name}"

    def get_username(self) -> str:
        return f"{self.last_name} {self.first_name}"


class CourseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = "Playwright"
    max_score: int = Field(alias="maxScore", default=1001)
    min_score: int = Field(alias="minScore", default=101)
    description: str = "Playwright course"
    preview_file: FileSchema = Field(alias="previewFile")
    estimatedTime: str = Field(alias="estimatedTime", default="21 weeks")
    created_by_user: UserSchema = Field(alias="createdByUser")


course_default_model = CourseSchema(
    id="course_id",
    title="Playwright3",
    maxScore=100,
    minScore=10,
    description="Playwright",
    previewFile=FileSchema(
        id="file-id",
        url="http://localhost:8000/",
        filename="file.png",
        directory="courses",
    ),
    estimatedTime="1 week",
    createdByUser=UserSchema(
        id="user-id",
        email="user@gmail.com",
        lastName="Bond",
        firstName="Zara",
        middleName="Alice"
    )
)
print('Course_default_model: ', course_default_model)

course_dict = {
    "id": "course_id2",
    "title": "Playwright3",
    "maxScore": 1004,
    "minScore": 105,
    "description": "Playwright6",
    "previewFile": {
        "id": "file-id",
        "url": "http://localhost:8000/",
        "filename": "file.png",
        "directory": "courses"
    },
    "estimatedTime": "17 week",
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Alice"
    }
}
course_dict_model = CourseSchema(**course_dict)
print('Course_dict model: ', course_dict_model)

course_json = """
{
    "id": "course_id2",
    "title": "Playwright3",
    "maxScore": 1004,
    "minScore": 105,
    "description": "Playwright6",
    "previewFile": {
        "id": "file-id",
        "url": "http://localhost:8000/",
        "filename": "file.png",
        "directory": "courses"
    },
    "estimatedTime": "17 week",
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Alice"
    }
}
"""
course_json_model = CourseSchema.model_validate_json(course_json)
print('Course JSON model: ', course_json_model)
print(course_json_model.model_dump())
print(course_json_model.model_dump_json())
print(course_json_model.model_dump(by_alias=True))

# course1 = CourseSchema()
# course2 = CourseSchema()
# print(course1.id)
# print(course2.id)

user=UserSchema(
    id="user-id",
    email="user@gmail.com",
    lastName="Bond",
    firstName="Zara",
    middleName="Alice"
)
print(user.get_username(), user.username)

try:
    file = FileSchema(
        id="file-id",
        url="1231http://localhost:8000",
        filename="file.png",
        directory="courses"
    )
except ValidationError as error:
    print(error)
    print(error.errors()) # Подробности по ошибке
