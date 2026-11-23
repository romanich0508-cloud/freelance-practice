import requests

відповідь = requests.get("https://api.github.com")
print(відповідь.status_code)