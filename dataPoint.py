#
# Data points will be captured periodically from sensors and this class
# will be used to hold that information

class DataPoint:
  captureTime = 0
  distance = 0
  direction = ""
  sensorId = ""
  
  def __init__(self, captureTime, distance, direction, sensorId):
    this.captureTime = captureTime
    this.distance = distance
    this.direction = direction
    this.sensorId = sensorId
