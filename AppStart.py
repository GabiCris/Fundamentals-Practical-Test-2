from AddressRepo import AddressRepo
from DriverRepo import DriverRepo
from Controller import Controller
from UI import UI


adrRepo = AddressRepo()
driverRepo = DriverRepo()

ctrl = Controller(adrRepo, driverRepo)

ui = UI (ctrl)

ui.menu()
