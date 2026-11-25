import httpx
from tools.fakers import fake

payload = {
    "email": get_random_email(),
    "password": "testPass123",
    "lastName": "Testov",
    "firstName": "User",
    "middleName": "Ivanovich"
}
response = httpx.post("http://localhost:8000/api/v1/users", json=payload)

print(response.status_code)
print(response.json())