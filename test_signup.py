import pytest
import requests


BASE_URL = "https://vigil.lendsqr.com/pecunia/api/v2/onboard"


user_data = {
    "business_name": "the",
    "email": "sundaycharles61@gmail.com",
    "locale": "en-US",
    "name": "John Doe",
    "password": "SecurePassword123!",
    "phone_number": "2347033490197",
    "rc_number": "6752",

}

def test_sign_up():
    response = requests.post(BASE_URL, json=user_data)


    print("Response Status Code:", response.status_code)
    print("Response Body:", response.text)


    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"


if __name__ == "__main__":
    pytest.main()
