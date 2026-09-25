import requests


BACKEND_URL = "http://127.0.0.1:8000"


def send_message(message: str) -> str:

    response = requests.post(
        f"{BACKEND_URL}/chat",
        json={"message": message},
        timeout=60,
    )

    response.raise_for_status()

    data = response.json()

    return data["response"]
