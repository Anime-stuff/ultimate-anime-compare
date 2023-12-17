import requests

def get_anime_details(anime_id):
    url = f"https://api.jikan.moe/v4/anime/{anime_id}/full"

    response = requests.get(url)

    if response.status_code == 200:
        anime_details = response.json()
        return anime_details
    else:
        print(f"Failed to fetch anime details. Status code: {response.status_code}")
        return None

anime_id = 457
anime_info = get_anime_details(anime_id)
print(anime_info)



# or using JikanPy
# from jikanpy import Jikan
# jikan = Jikan()
#
# mushishi = jikan.anime(457)
# print(mushishi)
