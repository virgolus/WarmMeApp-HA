# Install home assistant as docker container
docker run --init -d --name="home-assistant" -e "TZ=Europe/Rome" -v /Users/virgolus/Projects/homeassistant:/config -p 8123:8123 homeassistant/home-assistant:stable
