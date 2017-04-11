######################################
#
#
#
######################################

class LogicalUnit:
  sensorList = [] #A list that will contain all of the sensors
  motorController
  sensorData
  stopDistance = 20 #distance in centimeters
  currentDirection = "N"
  
  def readSensors(self):
    for sensor in sensorList:
      sensorData[sensor.name] = sensor.read()
      
  def start(self):
    while true:
      if(sensorData["FRONT"] < 20 && sensorData["FRONT"] != 0):
        motorController.setMode("STOP")
        if(sensorData["LEFT"] > sensorData["RIGHT"]):
          if(sensorData["LEFT"] != 0):
            motorController.setMode("LEFT")
            #Need to implement a way to turn for fixed time
        else:
          if(sensorData["RIGHT"] != 0):
            motorController.setMode("RIGHT")
            
      
            
    
    
    
  
  
  
