import requests

def get_top_anime():
    url = "https://api.jikan.moe/v4/top/anime?filter=bypopularity"
    params = {'page': 1}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        top_anime = response.json()
        print(top_anime)
    else:
        print(f"Failed to fetch top anime. Status code: {response.status_code}")
        return None

get_top_anime()
