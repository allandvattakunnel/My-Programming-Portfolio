class Transaction ():
    def __init__(self, transaction_id, type, amount, description,
                 status="Pending"):
        self.transaction_id = transaction_id
        self.type = type
        self.amount = amount
        self.description = description
        self.status = status

    def process_transaction(self):
        if self.status == "Pending":
            self.status = "Processed"
            return "This transaction has been processed!"
        # maybe add elif condition to return whether its been processed
        else:
            return "This transaction has already been processed!"

    def cancel_transaction(self):
        if self.status == "Pending":
            self.status = "Cancelled"
            return "This transaction has been cancelled."
        # maybe add elif condition to return whether its been processed/cancel
        else:
            return "The transaction has already been processed/cancelled."

    def update_description(self, description):
        self.description = description

    def __str__(self):
        ...


transaction_1 = Transaction(1, "Purchase", 100, "Buying gift card")
transaction_2 = Transaction(2, "Purchase", 250, "Buying an xbox")

print(transaction_1.process_transaction())
print(transaction_1.status)
print(transaction_1.cancel_transaction())

print(transaction_2.cancel_transaction())
print(transaction_2.status)
