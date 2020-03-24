import requests
import 

# Das Script arbeitet mit der Library "requests". Gegebenenfalls muss diese mit "pip install requests" nachinstalliert werden.
apiUrl = "https://api.ciscospark.com/v1/messages"
access_token = acess
httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}

body = {"toPersonEmail" : "gifbot@webex.bot", "text" : "Hello"}

response = requests.post(url=apiUrl, json=body, headers=httpHeaders)

print(response.status_code)
print(response.text)