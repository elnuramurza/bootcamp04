class Contact:
    all_contacts = [] 

    def __init__(self, name, lastname, phone_number):
        self.name = name
        self.lastname = lastname
        self.phone_number = phone_number
        Contact.all_contacts.append(self)

class Friend(Contact):
    def play_football_with_me(self):
        print(f"{self.name} is playing football with me!")

class ContactList(list):
    def search_by_name(self, name):
        matching_contacts = []
        for contact in self:
            if contact.name == name:
                matching_contacts.append(contact)
        return matching_contacts

contact1 = Contact("John", "Doe", "123-456-7890")
contact2 = Contact("Alice", "Smith", "987-654-3210")
contact3 = Contact("Bob", "Johnson", "555-123-4567")
friend1 = Friend("Charlie", "Brown", "111-222-3333")
friend2 = Friend("David", "Wilson", "444-555-6666")

contact_list = ContactList(Contact.all_contacts)
search_results = contact_list.search_by_name("John")
for contact in search_results:
    print(f"Found contact: {contact.name} {contact.lastname} ({contact.phone_number})")

search_results = contact_list.search_by_name("Charlie")
for contact in search_results:
    print(f"Found contact: {contact.name} {contact.lastname} ({contact.phone_number})")

friend1.play_football_with_me()

