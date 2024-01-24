import requests
import json
api_key = 'POD0qNqjfDrc4R9UMfYomEYpOCFjfYawFPE0TQ5L'
url = 'https://api.nasa.gov/your_endpoint'

params = {"api_key": api_key}

response = requests.get(url, params=json.dumps(params))
print(f"\nResponse:    {response.status_code}\nData Fetch:    {response.text()}\n")
