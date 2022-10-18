import os
import asyncio 
import requests 
from soheru import LOG, soheru
from soheru.database.client import startup


x = requests.get('http://api.soheru.in', allow_redirects=True).status_code
if x == 200:
    print(True)

for x in os.listdir("."):
    if "mp4" in x:
        os.remove(x)
    elif 'png' in x:
        os.remove(x)        
LOG.info('Cleaned Terminal')
    
soheru.start()
LOG.info('Started Bot')
startup()
LOG.info('Checked DB Startup')

loop = asyncio.get_event_loop()
loop.run_forever()
