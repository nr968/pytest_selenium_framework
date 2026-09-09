from utilities import api_handler

def test_register_user():
    response = api_handler.register_user("nk80001@gmail.com", "Password123")

    assert response.status_code == 201
    response_data = response.json()
    print(response_data)

    assert "token" in response_data
    assert response_data["token"] != ""
    assert "id" in response_data["user"]
    assert response_data["user"]["id"] != ""