
import requests

from Bot import LOG
anime_query = """
query ($id: Int, $idMal:Int, $search: String, $type: MediaType, $asHtml: Boolean) {
  Media (id: $id, idMal: $idMal, search: $search, type: $type) {
    id
    idMal
    title {
      romaji
      english
      native
    }
    format
    status
    description (asHtml: $asHtml)
    startDate {
      year
      month
      day
    }
    season
    episodes
    duration
    countryOfOrigin
    source (version: 2)
    trailer {
      id
      site
      thumbnail
    }
    coverImage {
      extraLarge
    }
    bannerImage
    genres
    averageScore
    nextAiringEpisode {
      airingAt
      timeUntilAiring
      episode
    }
    isAdult
    characters (role: MAIN, page: 1, perPage: 10) {
      nodes {
        id
        name {
          full
          native
        }
        image {
          large
        }
        description (asHtml: $asHtml)
        siteUrl
      }
    }
    studios (isMain: true) {
      nodes {
        name
        siteUrl
      }
    }
    siteUrl
  }
}
"""

url = 'https://graphql.anilist.co'

def animethumbnail(query):
    search = query
    variables = {'search': search, 'type': "ANIME"}
    json = requests.post(
        url, json={
            'query': anime_query,
            'variables': variables
        }).json()
    if 'errors' in json.keys():
        LOG.warn("[Error] No Thumbnail Exception Error.")
        image = "https://telegra.ph/file/ee05a623c981ccf5874a6.jpg"
        return image
    if json:
        json = json['data']['Media']
        anime_id = json['id']
        image = f"https://img.anili.st/media/{anime_id}"
    return image

def eng_name(query):
    search = query
    variables = {'search': search, 'type': "ANIME"}
    if search.isdigit():
        variables = {'id': int(search), 'type': "ANIME"}
        
    json = requests.post(
        url, json={
            'query': anime_query,
            'variables': variables
        }).json()
    if 'errors' in json.keys():
        ENGLISH_TITLE = 'None'
        return
    if json:
        json = json['data']['Media']
        ENGLISH_TITLE = f"{json['title']['english']}"
    return ENGLISH_TITLE

def jap_name(query):
    search = query
    variables = {'search': search, 'type': "ANIME"}
    
    if search.isdigit():
        variables = {'id': int(search), 'type': "ANIME"}
        
    json = requests.post(
        url, json={
            'query': anime_query,
            'variables': variables
        }).json()
    if 'errors' in json.keys():
        return
    if json:
        json = json['data']['Media']
        JAPANESE_TITLE = f"{json['title']['romaji']}"
    return JAPANESE_TITLE

def anime_id_get(query):
    search = query
    variables = {'search': search, 'type': "ANIME"}
    json = requests.post(
        url, json={
            'query': anime_query,
            'variables': variables
        }).json()
    if 'errors' in json.keys():
        return
    if json:
        json = json['data']['Media']
        ANIME_ID = json['id']
    return ANIME_ID
  
def anime_thumb(search):
    variables = {'search': search, 'type': "ANIME"}
    json = requests.post(
        url, json={
            'query': anime_query,
            'variables': variables
        }).json()
    if 'errors' in json.keys():
        return
    if json:
        json = json['data']['Media']
        coverImage = json['coverImage']['extraLarge']
        return coverImage