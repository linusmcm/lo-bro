import json
import requests

headers = {"Authorization": "Bearer 🔑 Your_API_Key"}

url = "https://api.edenai.run/v2/video/logo_detection_async"
json_payload = {
    "providers": "google",
    "file_url": "🔗 URL of your video"
}

response = requests.post(url, json=json_payload, headers=headers)

result = json.loads(response.text)
print(result)