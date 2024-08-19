import requests

url = "http://20.244.56.144/test/register"

data = {
    "companyName": "SR",
    "ownerName": "Charan Sai Anche",
    "rollNo": "2103A53001",
    "ownerEmail": "2103A53001@sru.edu.in",
    "accessCode": "CDGhzZ"
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Request successful!")
    print("Response data:", response.json())
else:
    print("Request failed with status code:", response.status_code)
    print("Response text:", response.text)