from client import Client


class Account:
    # Constructing the account class.
    def __init__(self, client, account_id, account_type, current_balance=0,
                 is_active=True):
        self.client = client
        self.account_id = account_id
        self.account_type = account_type
        self.current_balance = current_balance
        self.is_active = is_active

    def deposit(self,  deposit_amount):
        print(f"Your initial balance is: ${self.current_balance}")
        self.current_balance += deposit_amount
        print(f"Your new balance is: ${self.current_balance}")

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.current_balance:
            print(
                f"Insufficient Funds in {self.account_id}: your balance is: "
                f"$ {self.current_balance}")
        else:
            self.current_balance -= withdraw_amount
            print(f"Account {self.account_id}: withdrew ${withdraw_amount}.")
            print(f"The new balance is $ {self.current_balance}")

    def deactivate_account(self):
        if not self.is_active:
            print(f"Account:{self.account_id} has already been deactivated.")
            return
        else:
            self.is_active = False
            print(f"Account: {self.account_id} has now been deactivated")

    def __str__(self):
        return (f"Account {self.account_id} is owned by {self.client.name}"
                f" and has a balance of ${self.current_balance}.")


client_1 = Client("1", "Allan", "allan@gmail.com", "0423339567")


# Creating Account objects.
account_1 = Account(client_1, "1", "Savings", 22050)

print(account_1)
