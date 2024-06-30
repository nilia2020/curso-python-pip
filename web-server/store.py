import requests


def get_categories():
    r = requests.get("https://api.escuelajs.co/api/v1/categories")
    print(r.status_code)
    print(r.text)
    # Es una cadena, no puedo tratarlo como una lista
    print(type(r.text))
    # Lo convierto en una lista
    categories = r.json()
    print(type(categories))
    for category in categories:
        print(category["name"])
