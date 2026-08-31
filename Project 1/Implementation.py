# Creating the Client Class.
class Client:
    # Constructing the client class.
    def __init__(self, client_id, name, email, phone_number):
        self.client_id = client_id
        self.name = name
        self.email = email
        self.phone_number = phone_number

    # Creating a method to allow clients to update their email address.
    def update_email(self, new_email):
        # Assigning the new email value to self.email to store the new email for that specific Client object.
        self.email = new_email
        print(f"Your email has updated to: {new_email}")

    # Display the client's key information.
    def display_client_info(self):
        print(f"Client ID:{self.client_id}")
        print(f"Client Name: {self.name}")
        print(f"Client Email: {self.email}")
        print(f"Client Phone Number: {self.phone_number}")


client_1 = Client("1", "Allan", "allan@gmail.com", "042333")
client_1.display_client_info()
client_1.update_email("bananas@gmail.com")
client_1.display_client_info()

# Creating the Account class.
# account_id
# account_type
# opening_balance
# additional attribute - closing_balance


class Account:
    # Constructing the actual account class.
    def __init__(self, account_id, account_type, current_balance, closing_balance):
        self.account_id = account_id
        self.account_type = account_type
        self.current_balance = current_balance
        self.closing_balance = closing_balance

    def deposit(self, deposit_amount):
        print(f"Your initial balance is:")
        self.current_balance = self.current_balance + deposit_amount
        print(f"Your new current balance is: {self.current_balance}")

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.current_balance:
            print(
                f"Insufficient Funds in {self.account_id}: your balance is: {self.current_balance}")
        else:
            print(f"{self.account_id}: withdrew {withdraw_amount}.")
            print(f"The new balance is {self.current_balance}")


account_1 = Account("1", "Savings", "100", "200")
account_1.deposit("200")
