import requests

def register_user(api_url, email, password):
    payload = {
        "email": email,
        "password": password
    }

    return requests.post(url=f"{api_url}/auth/register", json=payload)

def login_user(api_url, email, password):
    payload = {
        "email": email,
        "password": password
    }

    return requests.post(url=f"{api_url}/auth/login", json=payload)