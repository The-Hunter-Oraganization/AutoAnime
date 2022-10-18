![AutoAnime](https://wallpaperaccess.com/full/2061.png)

# Soheru Kan
The name Soheru Kan translates to ("Sohail Khan") in Japanese, this bot was created by Sohail alone, no additional contributions. All credit goes to me.

</br>

We made this bot to automate the process of Telegram Anime Uploader, many kids there were dropping out and uploading anime for Weebs, so that they can watch anime without any hassle. To help them we make our private AutoPahe repo public

## Features 

```
[+] Make Sure You Add All These Mandatory Vars. 
    [-] Supports Multiple Channels. 
    [-] Update in Main Channel.
    [-] Add Sudos / Remove Sudos
    [-] Inbuilt Settings Disable/Enable Resolution.
    [-] Inbuilt restart command.
    [-] Easy deploy.
```

## Deploy

## Variables 
```
[+] Make Sure You Add All These Mandatory Vars. 
    [-] API_ID:   You can get this value from https://my.telegram.org
    [-] APP_HASH :   You can get this value from https://my.telegram.org
    [-] OWNER_ID : Your Telegram username. Without @.
    [-] BOT_TOKEN: Get from botfarther
    [-] MONGO_DB : get from cloud.mongodb.com.
    [-] ARCHIVE_CHANNEL: Your Archive Channel ID to store files (E.g -10037823545)
    [-] MAIN_CHANNEL: Your Main Channel Where Bot Will Update About Anime (E.g -10037823545)
    [-] MESSAGE_ID: Message Id of any message in main channel (E.g 40)'
[+] The Bot won't run without setting the mandatory vars.
```

### DOCKER DEPLOY

```
[-] git clone your_fork_url
[-] nano Bot/__init__.py edit variables (use (up and down keyboard buttons))
[-] docker build . -t autopahe
[-] docker run -d --restart on-failure --name autopahe autopahe
```

### Local Deploy

```
[-] apt install python3 python3-pip ffmpeg -y
[-] git clone your_fork_url
[-] cd AutoAnime 
[-] pip3 install -r requirements.txt
[-] nano Bot/__init__.py edit variables (use (up and down keyboard buttons))
[-] python3 -m Bot
```

### Heroku Deploy
<p align="center"><a href="https://heroku.com/deploy?template=https://github.com/The-Hunter-Oraganization/AutoAnime"> <img src="https://img.shields.io/badge/Deploy%20To%20Heroku-black?style=for-the-badge&logo=heroku" width="220" height="38.45"/></a></p>

## DEV / Soheru
### Contact

[• Github](https://github.com/soheru)</br>
[• Telegram](https://t.me/sohailkhan_indianime)</br>
[• Instagram](https://instagram.com/soherusan)</br>






