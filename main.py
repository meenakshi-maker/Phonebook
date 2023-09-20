def addNew():
    newFName = input("Enter FIRST Name: ")
    newLName = input("Enter LAST Name: ")
    newAddr = input("Enter ADDRESS: ")
    newCity = input("Enter CITY: ")
    newDist = input("Enter DISTRICT: ")
    newPhone = input("Enter PHONE: ")
    newDat = Contact(newFName, newLName, newAddr, newCity, newDist, newPhone)
    pBook.append(newDat)
    print("Contact Saved.")


def findContact():
    newFName = input("Enter FIRST Name: ")
    newLName = input("Enter LAST Name: ")

    # found = "Contact not found"
    found = 0

    for x in pBook:
        if x.FName == newFName and x.LName == newLName:
            found = x
            break
    return found


def editContact():
    toEdit = findContact()

    if toEdit != "Contact not found":
        print("1. Edit First Name")
        print("2. Edit Last Name")

        user1 = int(input("Enter Number: "))
        user2 = input("New value: ")

        if user1 == 1:
            toEdit.setFName(user2)
        else:
            toEdit.setLName(user2)

    print(toEdit)

    # menu to be created
    # get new input
    # use appropriate set method


""" 

     1. Edit First Name
     2. Edit Last Name
     3. Edit Address
     4. Edit City
     5. Edit District
     6. Edit Phone Number
     0. Go Back
     if choice == 0:
        break
     newDat = input("blah blah:  ")
     if choice == 1  
         toEdit.setFName(newDat)
     elif choice == 2  
          toEdit.setFName(newDat)
          """

from Contacts import Contact

pBook = []
# ---------------------->>>>>>>>>>>>CREATE CONTACT<<<<<<<<<<<<------------------------
dat11 = Contact("Harry", "Abraham", "8a Feltham Street", "Timaru", "Canterbury", "(020) 403 6704")
dat12 = Contact("Simon", "Brown", "75 Scott Street", "Blenheim", "Marlborough", "(027) 185 9643")
dat13 = Contact("Paul", "Abraham", "22 Tennyson Street", "Napier", "Hawke's Bay", "(029) 061 5554")
dat14 = Contact("Jonathan", "North", "41a Union Road", "Pukekohe", "Auckland", "(020) 632 1503")
dat15 = Contact("Theresa", "Morgan", "33a Waiouru Crescent", "Lower Hutt", "Wellington", "(021) 393 7110")
# -------------------->>>>>>>>>>>>>>>Load Phone book<<<<<<<<-----------------------
pBook.append(dat11)
pBook.append(dat12)
pBook.append(dat13)
pBook.append(dat14)
pBook.append(dat15)
# --------->>>>>>>>>>>>WORKIN AREA<<<<<<<<<<................
"""
something = findContact()
print(something)
"""
for x in pBook:
    print(x)

# editContact()


def addNew():
    newFName = input("Enter FIRST Name: ")
    newLName = input("Enter LAST Name: ")
    newAddr = input("Enter ADDRESS: ")
    newCity = input("Enter CITY: ")
    newDist = input("Enter DISTRICT: ")
    newPhone = input("Enter PHONE: ")
    newDat = Contact(newFName, newLName, newAddr, newCity, newDist, newPhone)
    pBook.append(newDat)
    print("Contact Saved.")


def findContact():
    newFName = input("Enter FIRST Name: ")
    newLName = input("Enter LAST Name: ")

    # found = "Contact not found"
    found = 0

    for x in pBook:
        if x.FName == newFName and x.LName == newLName:
            found = x
            break
    return found


def editContact():
    toEdit = findContact()

    if toEdit != "Contact not found":
        print("1. Edit First Name")
        print("2. Edit Last Name")

        user1 = int(input("Enter Number: "))
        user2 = input("New value: ")

        if user1 == 1:
            toEdit.setFName(user2)
        else:
            toEdit.setLName(user2)

    print(toEdit)

    # menu to be created
    # get new input
    # use appropriate set method


""" 

     1. Edit First Name
     2. Edit Last Name
     3. Edit Address
     4. Edit City
     5. Edit District
     6. Edit Phone Number
     0. Go Back
     if choice == 0:
        break
     newDat = input("blah blah:  ")
     if choice == 1  
         toEdit.setFName(newDat)
     elif choice == 2  
          toEdit.setFName(newDat)
          """

from Contacts import Contact

pBook = []
# ---------------------->>>>>>>>>>>>CREATE CONTACT<<<<<<<<<<<<------------------------
dat11 = Contact("Harry", "Abraham", "8a Feltham Street", "Timaru", "Canterbury", "(020) 403 6704")
dat12 = Contact("Simon", "Brown", "75 Scott Street", "Blenheim", "Marlborough", "(027) 185 9643")
dat13 = Contact("Paul", "Abraham", "22 Tennyson Street", "Napier", "Hawke's Bay", "(029) 061 5554")
dat14 = Contact("Jonathan", "North", "41a Union Road", "Pukekohe", "Auckland", "(020) 632 1503")
dat15 = Contact("Theresa", "Morgan", "33a Waiouru Crescent", "Lower Hutt", "Wellington", "(021) 393 7110")
# -------------------->>>>>>>>>>>>>>>Load Phone book<<<<<<<<-----------------------
pBook.append(dat11)
pBook.append(dat12)
pBook.append(dat13)
pBook.append(dat14)
pBook.append(dat15)
# --------->>>>>>>>>>>>WORKIN AREA<<<<<<<<<<................
"""
something = findContact()
print(something)
"""
for x in pBook:
    print(x)

# editContact()

