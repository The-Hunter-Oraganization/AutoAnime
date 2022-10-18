import json, requests
def telegraph_file_upload(path_to_file):
    file_types = {'gif': 'image/gif', 'jpeg': 'image/jpeg', 'jpg': 'image/jpg', 'png': 'image/png', 'mp4': 'video/mp4'}
    file_ext = path_to_file.split('.')[-1]
    
    if file_ext in file_types:
        file_type = file_types[file_ext]
    else:
        return f'error, {file_ext}-file can not be proccessed' 
      
    with open(path_to_file, 'rb') as f:
        url = 'https://graph.org/upload'
        response = requests.post(url, files={'file': ('file', f, file_type)}, timeout=1)
    try:
        telegraph_url = json.loads(response.content)
        telegraph_url = telegraph_url[0]['src']
        telegraph_url = f'https://graph.org/{telegraph_url}'
    except:
        telegraph_url = None 
    return telegraph_url