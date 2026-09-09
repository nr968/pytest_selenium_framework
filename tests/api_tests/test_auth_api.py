from utilities import api_handler


def test_register_user(api_url):
    response = api_handler.register_user(api_url,"nk80002@gmail.com", "Password123")

    assert response.status_code == 201
    response_data = response.json()

    assert "token" in response_data
    assert response_data["token"] != ""
    assert "id" in response_data["user"]
    assert response_data["user"]["id"] != ""

def test_invalid_email_register(api_url):
    response = api_handler.register_user(api_url,"abc123@gmail", "password123")

    assert response.status_code == 400
    response_data = response.json()

    assert "error" in response_data
    assert "details" in response_data
    assert response_data["details"][0]["field"] == "email"
    assert response_data["details"][0]["message"] == "A valid email is required"

def test_valid_user_login(api_url):
    response = api_handler.login_user(api_url, "nk80002@gmail.com", "Password123")

    assert response.status_code == 200
    response_data = response.json()

    assert "token" in response_data
    assert response_data["token"] != ""

    assert "id" in response_data["user"]
    assert response_data["user"]["id"] != ""
    assert isinstance(response_data["user"]["id"], int)

def test_valid_user_token(api_url):
    login_user_response = api_handler.login_user(api_url, "nk80002@gmail.com", "Password123")
    login_response = login_user_response.json()
    assert login_user_response.status_code == 200
    assert "token" in login_response
    token = login_response["token"]

    user_details_response= api_handler.get_user_identity_from_token(api_url, token)
    assert user_details_response.status_code == 200
    user_details = user_details_response.json()
    assert "user" in user_details
    assert "userId" in user_details["user"]
    assert user_details["user"]["userId"] != ""
    assert user_details["user"]["email"] == "nk80002@gmail.com"
