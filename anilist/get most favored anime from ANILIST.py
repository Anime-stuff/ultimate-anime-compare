import requests

query = '''
{
  Page {
    media(type: ANIME, sort:FAVOURITES_DESC) {
        title {
          romaji
          english
        }
        id
        idMal
        favourites
    }
  }
}
'''

url = 'https://graphql.anilist.co'

response = requests.post(url, json={'query': query})

print(response.json())
