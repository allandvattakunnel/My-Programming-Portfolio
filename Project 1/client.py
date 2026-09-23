class Client:
    # Constructing the client class.
    def __init__(self, client_id, name, email, phone_number):
        self.client_id = client_id
        self.name = name
        self.email = email
        self.phone_number = phone_number

    # Creating a method to allow clients to update their email address.
    def update_email(self, new_email):
        # Assigning the new email value to self.email to store the new email
        # for that specific Client object.
        self.email = new_email
        print(f"Your email has updated to: {new_email}")

    # Display the client's key information.
    def display_client_info(self):
        print(f"Client ID:{self.client_id}")
        print(f"Client Name: {self.name}")
        print(f"Client Email: {self.email}")
        print(f"Client Phone Number: {self.phone_number}")

    def __str__(self):
        return (f"Client: {self.name} can be contacted through"
                f" either email: {self.email} or phone: {self.phone_number}")

    def __repr__(self):
        return (f"Client(client_id ={self.client_id}, name = {self.name}"
                f" email = {self.email}, phone_number = {self.phone_number})")


client_1 = Client("1", "Allan", "allan@gmail.com", "0423339567")
print(client_1)
print(repr(client_1))
