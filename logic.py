######################################
#
#
#
######################################

class LogicalUnit:
  sensorList = [] #A list that will contain all of the sensors
  motorController
  sensorData
  
  def readSensors():
    for sensor in sensorList:
      sensorData[sensor.name].append(sensor.read())
      
  def turnLeft(degree):
    
    
    
  
  
  
