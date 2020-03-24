# Dieses Beispiel holt sich mittels eines Get Befehls die Räume des Nutzers mit dem angegebenen Access Token

# Das Script arbeitet mit der Library "requests". Gegebenenfalls muss diese mit "pip install requests" nachinstalliert werden.
import requests
import 

# Gemäss der API Dokumentation sind alle Aktionen bezüglich Räumen unter folgender URL abzurufen.
apiUrl = "https://api.ciscospark.com/v1/rooms"

# Das Access Token findet man unter "developer.webex.com"
access_token = access_token

# 
httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}

# Die folgenden Query Parameter sind optional
# queryParams = {"sortBy" : "lastactivity", "max" : "2"}
# response = requests.get(url=apiUrl, headers=httpHeaders, params=queryParams)

response = requests.get(url=apiUrl, headers=httpHeaders)

print(response.status_code)
print(response.text)
