import requests


url = "https://kitsu.io/api/graphql"
query = """
{
  findAnimeById(id: "3532") {
    averageRating
    averageRatingRank
    episodeLength
    favoritesCount
    id
    slug
    titles {
      alternatives
      canonical
      original
      romanized
      translated
    }
    totalLength
    type
    userCount
    userCountRank
  }
}
"""
response = requests.post(url, json={"query": query})

print(response.json())

# query animeByID($id: ID!) {
#     findAnimeById(id: $id) {
#         id
#         slug
#         createdAt
#         updatedAt
#         startDate
#         endDate
#         description
#         status
#         }
#     }
# }
#
#
# {"variables": {"id": 1 } }
