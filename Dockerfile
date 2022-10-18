FROM python:3.9.2-slim-buster
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ="Asia/Kolkata"
RUN apt -qq update && apt -qq install -y aria2 ffmpeg mediainfo tzdata git wget zip unzip build-essential
COPY . .
RUN python3 -m pip install --upgrade pip 
RUN pip3 install -r requirements.txt
CMD ["bash","run.sh"]
