import requests
from config import TOKEN, BASE_URL

def get_headers():
    return {'Authorization': f'OAuth {TOKEN}'}

def get_resources(path="/"):
    url = f"{BASE_URL}/resources"

    params = {"path": path}

    response = requests.get(url,headers=get_headers(), params=params)
    return response

def create_folder(path):
    url = f"{BASE_URL}/resources"
    params = {"path": path}

    response = requests.put(url,headers=get_headers(), params=params)
    return response

def delete_folder(path):
    url = f"{BASE_URL}/resources"

    params = {"path": path,
              "permanently": True}

    response = requests.delete(url, headers=get_headers(), params=params)

    return response

def public(path):
    url = f"{BASE_URL}/resources/publish"

    params = {"path": path}

    response = requests.put(url, headers=get_headers(), params=params)

    return response
