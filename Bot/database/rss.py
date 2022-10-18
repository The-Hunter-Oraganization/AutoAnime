from Bot.database.client import rss as db

def new(title, episode, episode_session):
    db.insert_one({'anime_title':title, 'episode':int(episode), 'episode_session':episode_session, 'status':'finished'})
    return True

def update(episode_session):
    x = db.update_one({'episode_session':episode_session}, {'$set':{'status':'finished'}})
    return True 

def find_pending():
    x = db.find({'status':'pending'})
    lsa = []
    for x in x:
        lsa.append((x['anime_title'], x['episode'], x['episode_session']))
    return lsa    

def check_pending(title, episode):
    x = db.find_one({'anime_title':title, 'episode':int(episode)})
    if x is not None:
        check = x['status']
        if check == 'finished':
            return True
        else:
            return False 
    else: 
        return False
