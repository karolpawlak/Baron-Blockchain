from app import app
from flask import render_template, request, jsonify
from app.transaction import Transaction

import Cryptodome
import Cryptodome.Random
import binascii
from Cryptodome.PublicKey import RSA

@app.route("/")
def index():
    return render_template("./index.html")


@app.route("/transactions")
def view_transactions():
    return render_template("./view_transactions.html")


@app.route("/transactions/new")
def new_transaction():
    return render_template("./make_transaction.html")


@app.route("/transactions/generate", methods=['POST'])
def generate_transaction():
    sender_address = request.form['sender_address']
    sender_private_key = request.form['sender_private_key']
    recipient_address = request.form['recipient_address']
    amount = request.form['amount']

    new_transaction = Transaction(sender_address, sender_private_key, recipient_address, amount)
    response = {
        'transaction': new_transaction.to_dictionary(),
        'signature': "signature"
    }

    return jsonify(response), 201


@app.route("/wallet/new")
def new_wallet():
    random_gen = Cryptodome.Random.new().read
    private_key = RSA.generate(1024, random_gen)  # specify key length (bits) and random generator
    public_key = private_key.public_key()

    response = {
        'public_key': binascii.hexlify(public_key.export_key(format('DER'))).decode('ascii'),
        'private_key': binascii.hexlify(private_key.export_key(format('DER'))).decode('ascii')
    }

    return jsonify(response), 200