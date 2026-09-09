import requests

base_url = "https://api.eventhub.rahulshettyacademy.com/api"

def register_user(email, password):
    payload = {
        "email": email,
        "password": password
    }

    response = requests.post(url=f"{base_url}/auth/register", json=payload)
    print(response.json())
    return response