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
        meanScore
        averageScore
        id
        idMal
        rankings {
          id
          rank
          context
          allTime
          type
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
