from dotenv import load_dotenv
load_dotenv()
import requests
import os 

# Das Script arbeitet mit der Library "requests". Gegebenenfalls muss diese mit "pip install requests" nachinstalliert werden.

access_token = os.getenv("ACCESSTOKEN")
room_ID = os.getenv("ROOMID")

apiUrl = "https://api.ciscospark.com/v1/messages"
httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}
body = {"roomId" : room_ID, "text" : "Testnachricht"}

response = requests.post(url=apiUrl, json=body, headers=httpHeaders)

print(response.status_code)
print(response.text)