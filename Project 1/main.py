from account import Account
from client import Client
from transaction import Transaction
from branch import Branch

# Creating Client objects.
client_1 = Client("1", "Allan", "allan@gmail.com", "0423339567")
client_2 = Client("2", "Jamie", "jamie23@outlook.com", "0466763903")
client_3 = Client("3", "Johnny", "johnny45@hotmail.com", "0434567340")

# Creating Account objects.
account_1 = Account(client_1, "1", "Savings", 22050)
account_2 = Account(client_2, "2", "Everyday", 30056)
account_3 = Account(client_3, "3", "Savings", 100000)

print(account_1.__str__())

# Printing selected attributes from each object.
# print(client_1.name)
# print(client_2.email)
# print(client_3.phone_number)
# print(account_1.account_id)
# print(account_2.account_type)
# print(account_3.current_balance)

# # Calling the Display and Update email methods for two client objects.
# client_1.display_client_info()
# client_1.update_email("allan1234@gmail.com")
# client_1.display_client_info()

# client_2.display_client_info()
# client_2.update_email("jamie3564@gmail.com")
# client_1.display_client_info()

# Adding funds for two accounts
account_1.deposit(200)
print(account_1.current_balance)
account_2.deposit(5000)
print(account_2.current_balance)

# Removing Funds from accounts
account_1.withdraw(100)
print(account_1.current_balance)
account_2.withdraw(1000000000)

branch_1 = Branch(1, "Adelaide Branch", "Adelaide", "0466764903", True)
branch_2 = Branch(2, "Noarlunga Branch", "Noarlunga", "0426478341")

print(branch_2.is_open)
print(branch_1.close_branch())
print(branch_2.is_open)
