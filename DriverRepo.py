from Domain import driver
class DriverRepo:
    def __init__(self):
        self._driverList = []
        self.fileRead()
        
    def fileRead(self):
        addressFile = open("driver.txt")
        
        for i in range (1,11):
            line = addressFile.readline()
            line = line.split(",")
            newDriver = driver(line[0], line[1], line[2])
            self._driverList.append(newDriver)
    '''      
    def getDriverById(self, id):
        for drivers in self._driverList:
            if drivers._id
    '''
    def __str__(self):
        msg =""
        for i in self._driverList:
            msg += str(i) + "\n"
        return msg
    