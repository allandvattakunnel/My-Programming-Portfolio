#Creating the Client Class

class Client:
    #constructing the client class
    def __init__(self,client_id,name,email,phone_number):
        self.client_id = client_id
        self.name = name
        self.email = email
        self.phone_number = phone_number

    #creating a method to allow clients to update their email address
    def update_email (self,new_email):
        print(f"Your email has updated to: {new_email}")

    #display the client's key info
    def display_client_info (self,client_id,name,email,phone_number):
        print(f"Client ID:{client_id}")
        print(f"Client Name: {name}")
        print(f"Client Email{email}")
        print(f"Client Phone Number{phone_number}")

allan = Client ("1","Allan","allan@gmail.com","042333")
allan.display_client_info()
allan.update_email("bananas@gmail.com")
allan.display_client_info()


