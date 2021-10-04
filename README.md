# WarmMeApp-HA
## Install docker containers
### Home Assistant
```
docker pull ghcr.io/home-assistant/raspberrypi3-homeassistant:stable
docker run -d \
  --name home-assistant \
  --privileged \
  --restart=unless-stopped \
  -e TZ=MY_TIME_ZONE \
  -v /home/pi/WarmMeApp-HA/homeassistant:/config \
  --network=host \
  ghcr.io/home-assistant/raspberrypi3-homeassistant:stable
```
### Home Assistant - HACS
Dalla dirrectory WarmMe-HA/homeassistant lanciareil comando
```
wget -q -O - https://install.hacs.xyz | bash -
```

### Mosquitto
```
docker run -it --name mosquitto -p 1883:1883 -v /home/pi/WarmMeApp-HA/mosquitto:/mosquitto/ --restart unless-stopped eclipse-mosquitto
```
## Properties
Copy warmme.properties.template as warmme.properties in the pi user home and fill the missing properties values.



