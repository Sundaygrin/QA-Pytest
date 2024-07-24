import pytest
import requests


BASE_URL = "https://vigil.lendsqr.com/pecunia/api/v2/auth/admin/login"

user_data = {
    "email": "sundaycharles61@gmail.com",
    "password": "Sunday@222"
}

def test_sign_in():
    response = requests.post(BASE_URL, json=user_data)

    # Print response content for debugging
    print("Response Status Code:", response.status_code)
    print("Response Body:", response.text)

    if response.status_code == 400:
        response_data = response.json()
        if response_data["message"] == "Redirecting to adjutor app":
            redirect_url = response_data["data"]["redirect_url"]
            print(f"Redirecting to: {redirect_url}")
            # Handle the redirect if needed, for example by making another request
            # redirected_response = requests.get(redirect_url)
            # print("Redirected Response Status Code:", redirected_response.status_code)
            # print("Redirected Response Body:", redirected_response.text)
            return

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

if __name__ == "__main__":
    pytest.main()