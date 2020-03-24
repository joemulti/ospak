import requests

# Das Script arbeitet mit der Library "requests". Gegebenenfalls muss diese mit "pip install requests" nachinstalliert werden.
apiUrl = "https://api.ciscospark.com/v1/messages"
access_token = "YzkwYWFjYWEtYmFkZi00ZThlLTk5M2YtOTg5MGFhYjhlZGM0OTA1ODU5OTMtZGNl_PF84_b26cc13b-37f7-4057-ab70-3e0f679db605"
httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}

body = {"toPersonEmail" : "gifbot@webex.bot", "text" : "Hello"}

response = requests.post(url=apiUrl, json=body, headers=httpHeaders)

print(response.status_code)
print(response.text)