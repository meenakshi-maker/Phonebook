
1.	This program is a basic phone book application that allows users to add and edit contacts. 
2.	The program first defines a class called "Contact" that represents a single contact with attributes such as first name, last name, address, city, district, and phone number. The class also includes methods to set and save these attributes. 
3.	The program then initializes an empty list called "pBook" to store all the contact objects. It also creates a few contact objects and adds them to the phone book list.
4.	The program includes three main functions:
  •	addNew(): This function prompts the user to enter details for a new contact and creates a new Contact object with the given details. The new contact is then added to the phone book list.
  •	findContact(): This function prompts the user to enter a first name and last name to search for a contact in the phone book list. If the contact is found, it returns the contact object. If not found, it returns 0.
  •	editContact(): This function calls the findContact() function to search for a contact. If the contact is found, it prompts the user to choose which attribute to edit (first name or last name) and then prompts for the new value. It then calls the appropriate set method of the Contact object to update the attribute.
The program also includes a loop that iterates through the phone book list and prints out the details of each contact.
