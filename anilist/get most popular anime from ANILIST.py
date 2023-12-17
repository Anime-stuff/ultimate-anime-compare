import requests

query = '''
{
  Page {
    media(type: ANIME, sort:POPULARITY_DESC) {
        id
        idMal
        popularity
        title {
          romaji
          english
          
        }
    }
  }
}
'''

url = 'https://graphql.anilist.co'

response = requests.post(url, json={'query': query})

print(response.json())
