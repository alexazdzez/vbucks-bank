from stock_vbucks import CompteApp
import requests

API_URL_REGISTER = "https://mvivibe.fr:5003/register"
API_URL_LOGIN = "https://mvivibe.fr:5003/login"

def add(username: str, password: str):
    data = {
        "username": username,
        "password": password
    }
    try:
        response = requests.post(API_URL_REGISTER, json=data)
        if response.status_code == 201:
            print("Inscription réussie !")
            return True
        else:
            print("Erreur :", response.json())
            return False
    except requests.exceptions.RequestException as e:
        print("Erreur réseau :", e)
        return False



def connect(username: str, password: str):
    data = {
        "username": username,
        "password": password
    }
    try:
        response = requests.post(API_URL_LOGIN, json=data)
        if response.status_code == 200:
            user_id = response.json().get("user_id")
            print(f"Connexion réussie ! user_id : {user_id}")
            CompteApp(user_id)
            CompteApp(user_id).mainloop()
            return user_id
        else:
            print("Erreur de connexion :", response.json())
            return None
    except requests.exceptions.RequestException as e:
        print("Erreur réseau :", e)
        return None