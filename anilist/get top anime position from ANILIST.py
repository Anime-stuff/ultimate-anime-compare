import requests

query = '''
query ($id: Int, $page: Int, $perPage: Int) {
    Page (page: $page, perPage: $perPage) {
        pageInfo {
            total
            currentPage
            lastPage
            hasNextPage
            perPage
        }
    media(id: $id, type: ANIME, sort:SCORE_DESC) {
        id
        idMal
        rankings {
          rank
          context
        }
        title {
          romaji
          english
        }
    }
  }
}
'''
variables = {
    'page': 1,
    'perPage': 1
}

url = 'https://graphql.anilist.co'

response = requests.post(url, json={'query': query, 'variables': variables})

print(response.json())
