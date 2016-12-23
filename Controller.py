class Controller():
    def __init__(self, addressRepo, driverRepo):
        self._addressRepo = addressRepo
        self._driverRepo = driverRepo
        
    '''
    FUNCTION that takes as param. an address and adds it to the Repo. IF the id is already
    in the repo, then the method raises an Exception
    '''
        
    def addAddress(self, address):
        self._addressRepo.addAddress(address)
        
    """
    FUNCTION that takes as param an id and returns the corresponding address.
    If no such address, the function returns an exception.
    """
    def getAddress(self, id):
        return self._addressRepo.getAddressId(id)
    
    
    '''
    FIND closest DRIVER function: Takes as Param an id and returns the
    closest driver to the location of the address corresponding to the ID
    
    return the driver which is closest to the address
    '''
    def findClosesetDriver(self, id):
        adr = self._addressRepo.getAddressId(id)
        valueList = []
        newList =[]
        
        for driver in self._driverRepo._driverList:
            dist = abs(int(adr._x) - int(driver._x)) + abs(int(adr._y) - int(driver._y))
            valueList.append(dist)
        
        minimum = min(valueList)
       
        for driver in self._driverRepo._driverList:
            dist = abs(int(adr._x) - int(driver._x)) + abs(int(adr._y) - int(driver._y))
            if dist == minimum:
                newDriver = driver
                break
        
        return driver  
        