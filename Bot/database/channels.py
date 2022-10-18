from Bot.database.client import channels as db

def add_new( anime_title, anime_id, id, title=None, filethumb=None, thumbnail=None):
    db.insert_one({'anime_title':anime_title, 'anime_id':int(anime_id), 'channel':int(id), 'filethumb':filethumb, 'wallpaper':thumbnail, 'customtitle':title})
    return True

def find_channel(anime_id):
    x = db.find_one({'anime_id':int(anime_id)})
    if x is not None:
        return x['channel'] 

def custom_file(anime_id):
    x = db.find_one({'anime_id':int(anime_id)})
    if x is not None:
        y = x['customtitle']
        if y == 'skip':
            return None
        else:
            return y 

def custom_thumb(anime_id):
    x = db.find_one({'anime_id':int(anime_id)})
    if x is not None:
        y = x['filethumb']   
        if y == 'skip':
            return None
        else:
            return y 
    
def custom_wall(anime_id):
    x = db.find_one({'anime_id':int(anime_id)})
    if x is not None:
        y = x['wallpaper'] 
        if y == 'skip':
            return None
        else:
            return y 
    
def remove(anime_id):
    db.find_one_and_delete({'anime_id':int(anime_id)})
    return True