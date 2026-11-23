import httpx


login_payload = {
    "email": "tuser@example.com",
    "password": "testPass123"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print("Login response: ", login_response_data)
print("Login status code: ", login_response.status_code)


access_token = login_response_data['token']['accessToken']
user_me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers={"Authorization": f"Bearer {access_token}"})
user_response_data = user_me_response.json()

print("User_me response: ", user_response_data)
print("User_me status code: ", user_me_response.status_code)