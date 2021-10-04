from datetime import date, datetime
import time
import threading

class sensor:
    def __init__(self,id,idHA):
        self.id=id
        self.idHA=idHA
        self.temp=""
        self.hum=""
        self.battery=""
        self.lastReading=""

    def updatevalue(self,value):
        test=False
        if "BATT" in value:
            self.battery=value[4:-1]
        if "TMPA" in value and not '-' in value:
            self.temp=value[4:]
        if "HUM" in value:
            self.hum=value[3:]
            test=True
        self.lastReading=datetime.now()
        return test

def findSensor(List,id):
    return next(x for x in List if x.id==id)

def timer(myListofSensors):
    checkSensorstatus(myListofSensors)
    threading.Timer(10,timer,args=[myListofSensors]).start()

def checkSensorstatus(ListofSensors):
    for sensor in ListofSensors:
        timeNow=datetime.now()
        timediff=timeNow-sensor.lastReading
        print timediff
        print timediff.days
        print timediff.seconds
        if timediff.seconds >60:
            print 'timeout!!!'

ListofSensors=[sensor('94','1'),
               sensor('96','2'),
               sensor('93','4')]

mySensor=findSensor(ListofSensors,'94')
mySensor.updatevalue('TMPA26')
time.sleep(2)
mySensor=findSensor(ListofSensors,'96')
mySensor.updatevalue('TMPA22')
time.sleep(2)
mySensor=findSensor(ListofSensors,'93')
mySensor.updatevalue('TMPA20')

timer(ListofSensors)
while True:
    print 'sto girando'
    time.sleep(2)
# timeNow=datetime.now()
# timediff=timeNow-mySensor.lastReading
# print(timediff)
# print(timediff.days)
# print(timediff.seconds)

