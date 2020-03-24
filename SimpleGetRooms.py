import requests
apiUrl = "https://api.ciscospark.com/v1/rooms"
access_token = "YzkwYWFjYWEtYmFkZi00ZThlLTk5M2YtOTg5MGFhYjhlZGM0OTA1ODU5OTMtZGNl_PF84_b26cc13b-37f7-4057-ab70-3e0f679db605"

httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}

# Die folgenden Query Parameter sind optional
# queryParams = {"sortBy" : "lastactivity", "max" : "2"}
# response = requests.get(url=apiUrl, headers=httpHeaders, params=queryParams)

response = requests.get(url=apiUrl, headers=httpHeaders)

print(response.status_code)
print(response.text)
