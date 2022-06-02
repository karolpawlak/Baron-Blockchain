from flask import Flask, render_template
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


# init
blockchain = Blockchain()

# node init
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("./index.html")

# def print_hi(name):
#     print(f'Hi, {name}')
#
#


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5001, type=int, help="Specify the port to listen to with --port or -p")
    args = parser.parse_args()
    port = args.port

    app.run(host='127.0.0.1', port=port, debug=True)

