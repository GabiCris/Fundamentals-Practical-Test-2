from Domain import address
class AddressRepo:
    def __init__(self):
        self._addressList = []
        self.fileRead()
        
    def fileRead(self):
        addressFile = open("address.txt")
        
        for i in range (1,11):
            line = addressFile.readline()
            line = line.split(",")
            
            newAddress = address(line[0], line[1], line[2], line[3])
            self._addressList.append(newAddress)
        
    def addAddress(self, address):
        if self.searchId(address.getId()):
            raise Exception("There is already an address with that ID!")
        self._addressList.append(address)
        
    def searchId(self, id):
        for add in self._addressList:
            if id == add.getId():
                return True
        return False
    
    def getAddressId(self, id):
        for add in self._addressList:
            if id == add.getId():
                return add
        raise Exception("NO SUCH address!!")
    
    def __str__(self):
        msg =""
        for i in self._addressList:
            msg += str(i) + "\n"
        return msg
    
