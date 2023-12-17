import requests

def get_top_anime():
    url = "https://kitsu.io/api/edge/anime?fields[anime]=slug,canonicalTitle,titles,favoritesCount&sort=-favoritesCount&page[limit]=1"

    response = requests.get(url)

    if response.status_code == 200:
        top_anime = response.json()
        print(top_anime)
    else:
        print(f"Failed to fetch highest rated anime. Status code: {response.status_code}")
        return None

get_top_anime()
