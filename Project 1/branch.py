class Branch ():
    def __init__(self, number, name, suburb, phone_number, is_open=False):
        self.number = number
        self.name = name
        self.suburb = suburb
        self.phone_number = phone_number
        self.is_open = is_open

    def open_branch(self):
        if not self.is_open:
            self.is_open = True
            # add branch id
            return "This branch has been opened"
        else:
            # add branch id
            return "This branch is already open!"

    def close_branch(self):
        if self.is_open:
            self.is_open = False
            return "This branch has now closed."
        else:
            return "This branch is already closed!"

    def update_phone_number(self, phone_number):
        self.phone_number = phone_number
        return f"The new branch phone number is {self.phone_number}"


# branch_1 = Branch(1, "Adelaide Branch", "Adelaide", "0466764903", True)
# branch_2 = Branch(2, "Noarlunga Branch", "Noarlunga", "0426478341")

# print(branch_2.is_open)
# print(branch_1.close_branch())
# print(branch_2.is_open)
