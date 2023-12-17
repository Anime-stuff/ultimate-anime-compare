import requests

def get_anime_data():
    url = "https://kitsu.io/api/edge/anime/3532"
    response = requests.get(url)

    if response.status_code == 200:
        anime_data = response.json()
        print(anime_data)
    else:
        print(f"Failed to fetch anime data. Status code: {response.status_code}")
        return None

get_anime_data()
