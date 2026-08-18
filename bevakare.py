import requests

urls = {
    "Laptop Outlet": "https://www.elgiganten.se/outlet/outlet-datorer-kontor/outlet-laptop/page-1",
    "Gaming Laptop Outlet": "https://www.elgiganten.se/outlet/outlet-gaming/outlet-gaming-laptop"
}

headers = {
    "User-Agent": "Mozilla/5.0"
}

for name, url in urls.items():
    print()
    print("=" * 50)
    print(name)
    print(url)
    print("=" * 50)

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=20
        )

        print("Statuskod:", response.status_code)
        print("Antal tecken:", len(response.text))

    except Exception as e:
        print("Fel:", e)
