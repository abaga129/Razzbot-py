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
  decisionList = []
  
  def readSensors(self):
    for sensor in sensorList:
      sensorData[sensor.name] = sensor.read()
      
  def start(self):
    decision = ""
    while true:
      readSensors()
      
      #Check if front sensor is less than 20cm from an object
      if(sensorData["FRONT"] < 20 and sensorData["FRONT"] != 0):
        decision = "STOP"
        motorController.setMode(decision)
        
        #If distance on left > distance on right
        if(sensorData["LEFT"] > sensorData["RIGHT"]):
          if(sensorData["LEFT"] != 0):
            decision = "LEFT"
            motorController.setMode(decision)
        
        #If distance on right > distance on left
        else:
          if(sensorData["RIGHT"] != 0):
            decision = "RIGHT"
            motorController.setMode(decision)
      
      #Check if Left sensor reads less than 10cm  
      elif(sensorData["LEFT"] < 10 and sensorData["LEFT"] != 0):
        decision = "STOP"
        motorController.setMode(decision)
        #Check if right sensor reads greater than 10 : if so turn right
        if(sensorData["RIGHT"] > 10 and sensorData["RIGHT"] != 0):
          decision = "RIGHT"
          motorController.setMode(decision) 
        #Otherwise back up
        else:
          decision = "BACKWARD"
          motorController.setMode(decision)
      
      #Check if Right sensor reads less than 10cm
      elif(sensorData["RIGHT"] < 10 and sensorData["RIGHT"] != 0):
        decision = "STOP"
        motorController.setMode(decision)
        if(sensorData["LEFT"] > 10):
          decision = "LEFT"
          motorController.setMode(decision)
        else:
          decision = "BACKWARD"
          motorController.setMode(decision)
          
      else:
        decision = "FORWARD"
        motorController.setMode(decision)
        
      decisionList.append(decision)
      
      time.sleep(0.1)
          
