class Contact:
    def __init__(self, newFName, newLName, newAddr, newCity, newDist, newPhone):
        self.FName = newFName
        self.LName = newLName
        self.newAddr = newAddr
        self.newCity = newCity
        self.newDist = newDist
        self.Phone = newPhone

    def setFName(self, otherFName):
        self.FName = otherFName

    def setLAddr(self, otherAddr):
        self.Addr = otherAddr

    def setLName(self, otherCity):
        self.City = otherCity

    def setLName(self, otherDist):
        self.Dist = otherDist

    def __str__(self):
        return (f"\nFirst Name: {self.FName}\n"
                f"Last Name:     {self.LName}\n"
                f"Addr:          {self.newAddr}\n"
                f"City:          {self.newCity}\n"
                f"District:      {self.newDist}\n"
                f"Phone:         {self.Phone}")


