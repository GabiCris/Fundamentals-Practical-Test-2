import cmd
from Domain import address


class UI:
    def __init__(self, ctrl):
        self._controller = ctrl
    @staticmethod
    def printMenu():
        msg = ""
        msg+= "1. ADD Address\n"
        msg+= "2. Display Addresses\n"
        msg+= "3. Display Drivers\n"
        msg+= "4. Find Closest Driver\n"
        msg+= "0. EXIT\n"
        return msg
        
    @staticmethod
    def get_cmd():
        cmd = input("Please input command:")
        return cmd
    
    def menu(self):
        alive = True
        print("Welcome!! \n")
        while alive:
            try:
                print(self.printMenu())
                cmd = self.get_cmd()
                if cmd == '1':
                    self.f_addAddress()
                if cmd == '2':
                    self.f_printAddress()
                if cmd == '3':
                    self.f_printDriver()
                if cmd =='4':
                    self.f_findDriver()
                    
                if cmd == '0':
                    exit()
            except Exception as x:
                print(x)
                    
    
    def f_addAddress(self):
        id = input("Address ID: ")
        name = input("Name: ")
        x = input("X: ")
        y = input("Y: ")
        
        newAddress = address(id, name, x, y)
        self._controller.addAddress(newAddress)
        
    def f_printAddress(self):
        print(self._controller._addressRepo)
        
    def f_printDriver(self):
        print(self._controller._driverRepo)
        
    def f_findDriver(self):
        id = input("Address ID: ")
        print("Driver: ", self._controller.findClosesetDriver(id)._driverName)
        print("Address: ", self._controller.getAddress(id)._adrName)
    
        
