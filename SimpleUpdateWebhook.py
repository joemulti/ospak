#Dieses Programm ist am Anfang eines Tages einmalig auszuführen- oder wenn sich die ngrok URL geändert hat
from dotenv import load_dotenv
load_dotenv()
import requests
import os 

# Das Script arbeitet mit der Library "requests". Gegebenenfalls muss diese mit "pip install requests" nachinstalliert werden.
access_token = os.getenv("ACCESSTOKEN")
webhookID = os.getenv("WEBHOOKID")
ngrokurl = os.getenv("NGROKURL")
roomId = os.getenv("ROOMID")
httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}
apiUrl = "https://api.ciscospark.com/v1/webhooks/" + webhookID
body = {"name" : "MeinTestwebhook", "targetUrl" : ngrokurl, "resource" : "all","filter":"roomID="+roomId}

response = requests.put(url=apiUrl, json=body, headers=httpHeaders)

print(response.status_code)
print(response.text)