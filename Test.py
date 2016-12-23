
import unittest
from AddressRepo import AddressRepo
from DriverRepo import DriverRepo
from Controller import Controller
from Domain import address


class Test(unittest.TestCase):

    def setUp(self):
        addressRepo = AddressRepo()
        driverRepo = DriverRepo()
        self._ctrl = Controller(addressRepo, driverRepo)
    
    def testName(self):
        self.assertEqual(len(self._ctrl._addressRepo._addressList), 10)
        self._ctrl.addAddress(address('1678','luceafarului','11','15'))
        self.assertEqual(len(self._ctrl._addressRepo._addressList), 11)
        self._ctrl.addAddress(address('1798','luceafarului','11','15'))
        self.assertEqual(len(self._ctrl._addressRepo._addressList), 12)
        
        self.assertRaises(Exception,self._ctrl.addAddress, address('1','luceafarului','11','15'))
        
        driver = self._ctrl.findClosesetDriver("17")
        self.assertEqual(driver._driverName, "maria")
        driver = self._ctrl.findClosesetDriver("377")
        self.assertEqual(driver._driverName, "sofita")
        driver = self._ctrl.findClosesetDriver("13")
        self.assertEqual(driver._driverName, "bogdan")


        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()