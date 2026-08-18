import requests

urls = {
    "RTX 5070": "https://www.elgiganten.se/brand/nvidia/nvidia-geforce-50-series/nvidia-geforce-rtx-5070-series/page-1",
    "RTX 5060": "https://www.elgiganten.se/brand/nvidia/nvidia-geforce-50-series/nvidia-geforce-rtx-5060-serien/page-1"
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

        if response.status_code == 200:
            print("Sidan kunde hämtas!")
        else:
            print("Sidan kunde inte hämtas.")

    except Exception as e:
        print("Fel:", e)
