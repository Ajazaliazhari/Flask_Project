import requests

api_key = 'POD0qNqjfDrc4R9UMfYomEYpOCFjfYawFPE0TQ5L'
url = 'https://api.nasa.gov/your_endpoint'

params = {
    'api_key': api_key,
}

response = requests.get(url, params=params)

if response.status_code == 200:
    print(f"\nResponse:    {response.status_code}\nData Fetch:    {response.text}\n")
else:
    print(f"Error: {response.status_code}\n{response.text}\n")

