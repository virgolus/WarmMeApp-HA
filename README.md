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
  ghcr.io/home-assistant/raspberrypi3-homeassistant:2022.10.5
```

### Home Assistant - HACS
Dalla directory WarmMe-HA/homeassistant lanciare il comando
```
wget -q -O - https://install.hacs.xyz | bash -
```

### Mosquitto
```
docker run -it --name mosquitto -p 1883:1883 -v /home/pi/WarmMeApp-HA/mosquitto:/mosquitto/ --restart unless-stopped eclipse-mosquitto
```

## Properties
Copy warmme.properties.template as warmme.properties in the pi user home and fill the missing properties values.

## Swap file dimension
```
sudo nano /etc/dphys-swapfile
CONF_SWAPSIZE=2048
sudo dphys-swapfile setup
sudo dphys-swapfile swapon
```

### WarmMe core
- cd /home/pi/WarmMeApp-HA/warmme
- pip install -r requirements.txt

## Raspy serial config
from raspy-config cli, follow this guide
https://jemrf.github.io/RF-Documentation/configure_serial_port.html

### Autostart
For all files in directory WarmMeApp-HA/scripts/autostart_services:
```
- copy script into /etc/systemd/system/
- sudo chmod 644
- sudo systemctl daemon-reload
- sudo systemctl enable name-of-your-service.service
```

## Logrotate
copy files from .scripts/logrotate to /etc/logrotate.d/

## Crontab 
```
0 22 * * mon docker restart home-assistant >> /home/pi/WarmMeApp-HA/logs/crontab.log 2>&1
0 23 * * mon systemctl restart tunnel-bagolino.service >> /home/pi/WarmMeApp-HA/logs/crontab.log 2>&1
0 23 * * mon systemctl restart warmme-core.service >> /home/pi/WarmMeApp-HA/logs/crontab.log 2>&1
```

# Mappatura cavi quadro mamma
0 caldaia
1 sopra
2 sotto
3 bagno
4 laboratorio






