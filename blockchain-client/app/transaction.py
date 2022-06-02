from collections import OrderedDict


class Transaction:
    def __init__(self, sender_address, sender_private_key, recipient_address, amount):

        self.sender_address = sender_address
        self.sender_private_key = sender_private_key
        self.recipient_address = recipient_address
        self.amount = amount

    def to_dictionary(self):
        return OrderedDict({
            'sender_address': self.sender_address,
            'sender_private_key': self.sender_private_key,
            'recipient_address': self.recipient_address,
            'amount': self.amount
        })