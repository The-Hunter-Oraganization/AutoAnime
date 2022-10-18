from Bot.database.client import users as db

def new_user(id, auth=False):
    db.insert_one({'userid':int(id), 'auth':bool(auth)})
    return True

def is_reg(id):
    x = db.find_one({'userid':int(id)})
    if x is not None:
        return True 
    else:
        return False 
 
def get_auth(id):
    x = db.find_one({'userid':id}) 
    if x is not None:
        return x['auth']
    else:
        return False 
    
def update_user(id, auth=False):
    db.update_one({'userid':int(id)}, {'$set':{'auth':bool(auth)}})   
    return True 
