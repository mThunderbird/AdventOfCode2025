import os
import requests
from requests import Session

SESSION = "53616c7465645f5fa423ad8b2fbfedfac4e3f9431497ce367b644dd609f6d7b431c61c2222ae4b1a36780a645b2a69f5aab0eca2c71ce17e1baa2eb20ba3af7f"

def fetch_input(url):

    session = SESSION
    r = requests.get(url, cookies={"session": session})
    r.raise_for_status()
    return r.text.strip()