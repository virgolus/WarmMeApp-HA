# WarmMeApp-HA
## Install docker containers
### Home Assistant
```
docker run --init -d --name="home-assistant" -e "TZ=Europe/Rome" -v /home/pi/homeassistant:/config --net=host --restart unless-stopped  homeassistant/raspberrypi3-homeassistant:stable
```
### Mosquitto
```
docker run -it --name mosquitto -p 1883:1883 -v /home/pi/WarmMeApp-HA/mosquitto:/mosquitto/ --restart unless-stopped eclipse-mosquitto
```
## Properties
Copy warmme.properties.template as warmme.properties in the pi user home and fill the missing properties values.



