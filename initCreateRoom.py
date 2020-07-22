# SimpleCreateRoom
from dotenv import load_dotenv
load_dotenv()
import requests
import os

# Das Script arbeitet mit der Library "requests". Gegebenenfalls muss diese mit "pip install requests" nachinstalliert werden.

def main():

    apiUrl = "https://api.ciscospark.com/v1/rooms"
    access_token = os.getenv("ACCESSTOKEN")
    httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}

    body = {"title" : str(os.getenv("CLASSPREFIX")) + " " + "Testraum WebexTeams API Kurs"}

    response = requests.post(url=apiUrl, json=body, headers=httpHeaders)


    print(response.status_code)
    print(response.text)

main()