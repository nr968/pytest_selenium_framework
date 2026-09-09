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

def get_user_identity_from_token(api_url, token):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    return requests.get(url=f"{api_url}/auth/me", headers=headers)