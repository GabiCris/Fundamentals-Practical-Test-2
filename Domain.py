
class address:
    def __init__(self, adrId, name, x, y):
        self._id = adrId
        self._adrName = name
        self._x = x
        self._y = y
        
    def getId(self):
        return self._id
    
    def __str__(self):
        return "Address ID: " + self._id +", Name: " + self._adrName + ", x: " +self._x + ", y: " +self._y 
    
    
class driver:
    def __init__(self, name, x, y):
        self._driverName = name
        self._x = x
        self._y = y
        
    def getDriverName(self):
        return self._driverName
    def getDriverX(self):
        return self._x
    def getDriverY(self):
        return self._y
    
    def __str__(self):
        return "Driver Name: " + self._driverName + ", x: " +self._x + ", y: " +self._y
    