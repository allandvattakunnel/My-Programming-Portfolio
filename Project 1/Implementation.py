# # Creating the Client Class.
# class Client:
#     # Constructing the client class.
#     def __init__(self, client_id, name, email, phone_number):
#         self.client_id = client_id
#         self.name = name
#         self.email = email
#         self.phone_number = phone_number

#     # Creating a method to allow clients to update their email address.
#     def update_email(self, new_email):
#         # Assigning the new email value to self.email to store the new email for that specific Client object.
#         self.email = new_email
#         print(f"Your email has updated to: {new_email}")

#     # Display the client's key information.
#     def display_client_info(self):
#         print(f"Client ID:{self.client_id}")
#         print(f"Client Name: {self.name}")
#         print(f"Client Email: {self.email}")
#         print(f"Client Phone Number: {self.phone_number}")


# class Account:
#     # Constructing the actual account class.
#     def __init__(self, account_id, account_type, current_balance=0, is_active=True):
#         self.account_id = account_id
#         self.account_type = account_type
#         self.current_balance = current_balance
#         self.is_active = is_active

#     def deposit(self, deposit_amount):
#         print(f"Your initial balance is: ${self.current_balance}")
#         self.current_balance += deposit_amount
#         print(f"Your new balance is: ${self.current_balance}")

#     def withdraw(self, withdraw_amount):
#         if withdraw_amount > self.current_balance:
#             print(
#                 f"Insufficient Funds in {self.account_id}: your balance is: $ {self.current_balance}")
#         else:
#             self.current_balance -= withdraw_amount
#             print(f"Account {self.account_id}: withdrew ${withdraw_amount}.")
#             print(f"The new balance is $ {self.current_balance}")

#     def deactivate_account(self):
#         if not self.is_active:
#             print(f"Account:{self.account_id} has already been deactivated.")
#             return
#         else:
#             self.is_active = False
#             print(f"Account: {self.account_id} has now been deactivated")


# # Creating Client objects.
# client_1 = Client("1", "Allan", "allan@gmail.com", "0423339567")
# client_2 = Client("2", "Jamie", "jamie23@outlook.com", "0466763903")
# client_3 = Client("3", "Johnny", "johnny45@hotmail.com", "0434567340")

# # Creating Account objects.
# account_1 = Account("1", "Savings", 22050)
# account_2 = Account("2", "Everyday", 30056)
# account_3 = Account("3", "Savings", 100000)

# # Printing selected attributes from each object.
# # print(client_1.name)
# # print(client_2.email)
# # print(client_3.phone_number)
# # print(account_1.account_id)
# # print(account_2.account_type)
# # print(account_3.current_balance)

# # # Calling the Display and Update email methods for two client objects.
# # client_1.display_client_info()
# # client_1.update_email("allan1234@gmail.com")
# # client_1.display_client_info()

# # client_2.display_client_info()
# # client_2.update_email("jamie3564@gmail.com")
# # client_1.display_client_info()

# # Adding funds for two accounts
# account_1.deposit(200)
# print(account_1.current_balance)
# account_2.deposit(5000)
# print(account_2.current_balance)

# # Removing Funds from accounts
# account_1.withdraw(100)
# print(account_1.current_balance)
# account_2.withdraw(1000000000)
