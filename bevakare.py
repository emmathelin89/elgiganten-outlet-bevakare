import requests

url = "https://www.elgiganten.se/outlet"

response = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=20
)

print("Statuskod:", response.status_code)
print("Antal tecken:", len(response.text))

if response.status_code == 200:
    print("Elgigantens sida kunde hämtas!")
else:
    print("Något gick fel.")
