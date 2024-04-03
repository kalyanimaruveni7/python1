contacts={
    "Ram":{
        "phone":"1234-567-890",
        "email":"ram18@gmail.com",
        "address":"1/1 mk street,nagari,India"
    },
    "sita":{
        "phone":"1234-567-890",
        "email":"sita@gmail.com",
        "address":"1/2 mk street,nagari,India"
    }
}
def add_contact(name,phone,email,address):
    contacts[name]={
        "phone":phone,
        "email":email,
        "address":address
    }
    print("Contact added successfully!!")
def view_contacts():
    for name,contact in contacts.items():
        print(f"Name:{name}")
        print(f"Phone:{contact['phone']}")
        print(f"Email:{contact['email']}")
        print(f"Address:{contact['address']}")
        return
    print("Any contacts not found")
def update_contact(name, phone=None, email=None, address=None):
    if name in contacts:
        contact = contacts[name]
        if phone:
            contact['phone'] = phone
        if email:
            contact['email'] = email
        if address:
            contact['address'] = address
        print("Contact updated successfully!")
    else:
        print("Contact not found.")
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully")
    else:
        print("Contact not found!!")
add_contact("yamu",2614357,"yamu@gmail.com","street")
view_contacts()
update_contact({"yamu":"yamuna"})
del contacts["Ram"]
