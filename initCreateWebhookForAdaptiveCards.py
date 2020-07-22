#Dieses Programm ist am Anfang eines Tages einmalig auszuführen- oder wenn sich die ngrok URL geändert hat
from dotenv import load_dotenv
load_dotenv()
import requests
import os 

# Das Script arbeitet mit der Library "requests". Gegebenenfalls muss diese mit "pip install requests" nachinstalliert werden.
access_token = os.getenv("ACCESSTOKEN")
ngrokurl = os.getenv("NGROKURL")
roomId = os.getenv("ROOMID")
prefix = os.getenv("CLASSPREFIX")
webhookname = "Teams API Kurs Attachment Webhook"
httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}
apiUrl = "https://api.ciscospark.com/v1/webhooks/"
body = {"name" : str(prefix) +' '+ webhookname, "targetUrl" : ngrokurl, "resource" : "attachmentActions","filter":"roomId="+roomId,"event":"created"}

response = requests.post(url=apiUrl, json=body, headers=httpHeaders)

print(response.status_code)
print(response.text)