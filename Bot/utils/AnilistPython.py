
import requests

from Bot import LOG

def animethumbnail(query):
    x = requests.get(f'http://api.soheru.in/anime/{query}').json().get('data').get('Media').get('id')
    image = f"https://img.anili.st/media/{x}"
    return image

def eng_name(query):
  x = requests.get(f'http://api.soheru.in/anime/{query}').json().get('data').get('Media').get('title').get('english')
  return x

def jap_name(query):
  x = requests.get(f'http://api.soheru.in/anime/{query}').json().get('data').get('Media').get('title').get('romaji')
  return x

def anime_id_get(query):
  x = requests.get(f'http://api.soheru.in/anime/{query}').json().get('data').get('Media').get('id')
  return x
  
def anime_thumb(search):
  x = requests.get(f'http://api.soheru.in/anime/{search}').json().get('data').get('Media').get('coverImage').get('extraLarge')
  return x