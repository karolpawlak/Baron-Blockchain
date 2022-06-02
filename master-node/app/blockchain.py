from time import time


class Blockchain:

    def __init__(self):

        self.transactions = []
        self.chain = []
        self.create_block(0, '00')  # genesis block creation

    # add a block of transactions to the blockchain
    def create_block(self, nonce, previous_hash):

        block = {'block_number': len(self.chain) + 1,
                 'timestamp': time(),
                 'transactions': self.transactions,
                 'nonce': nonce,
                 'previous_hash': previous_hash
        }

        # reset transactions
        self.transactions = []

        # append a block
        self.chain.append(block)
