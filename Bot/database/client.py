from pymongo import MongoClient 
from Bot import DATABASE_URL, OWNER_ID

clientdb = MongoClient(DATABASE_URL)
typedb = clientdb['SoheruGroup']
users = typedb['users']
channels = typedb['channels']
globaldb = typedb['globaldb']
rss = typedb['rss']

def startup():
    x = globaldb.find_one({'setup_done':True})
    if x is not None:
        return 
    fileformat('[IA] [episode - title] [resolution] [Sub].mkv')
    globaldb.insert_one({'resolution':'360p', 'auth':bool(True)})
    globaldb.insert_one({'resolution':'480p', 'auth':bool(True)})
    globaldb.insert_one({'resolution':'720p', 'auth':bool(True)})
    globaldb.insert_one({'resolution':'1080p', 'auth':bool(True)})
    users.insert_one({'userid':int(OWNER_ID), 'auth':bool(True)})
    globaldb.insert_one({'setup_done':True})
    return True 
   
 
    
def fileformat(query):
    globaldb.insert_one({'fileformat':query, 'file':True})
    return True 

def update_format(query):
    globaldb.update_one({'fileformat':query})

def enable_resolution(resolution, yes):
    globaldb.update_one({'resolution':resolution, 'auth':bool(yes)})
    return True 

def check_resolution(resolution):
    x = globaldb.find_one({'resolution':resolution})
    if x is not None:
       return x['auth']
     
def currentformat():
    x = globaldb.find_one({'file':True})
    if x is not None:
        return x['fileformat']
    else:
        return None
        
            
    
    
    
    
    