# import BigchainDB and create an object
from bigchaindb_driver import BigchainDB
bdb_root_url = 'http://localhost:9984'
bdb = BigchainDB(bdb_root_url)
import json
# generate a keypair
from bigchaindb_driver.crypto import generate_keypair
sendr, recvr = generate_keypair(), generate_keypair()
print(sendr)
# create a digital asset for Alice
ddr_token = {
    'data': {
        'token_for': {
            'ddr': {
                'serial_number': 'LR1234'
            }
        },
        'description': 'Money transfer token where 1 token is equivalent to 1 INR.',
    },
}

# prepare the transaction with the digital asset and issue 10 tokens for recvr
prepared_token_tx = bdb.transactions.prepare(
    operation='CREATE',
    signers=sendr.public_key,
    recipients=[([recvr.public_key], 10)],
    asset=ddr_token)

    
print("sendr.private_key",sendr.private_key)
# fulfill and send the transaction
fulfilled_token_tx = bdb.transactions.fulfill(
    prepared_token_tx,
    private_keys=sendr.private_key)
sent=bdb.transactions.send_commit(fulfilled_token_tx)
print(json.dumps(sent,indent=3))
# Use the tokens
# create the output and inout for the transaction
transfer_asset = {'id': fulfilled_token_tx['id']}
output_index = 0
output = fulfilled_token_tx['outputs'][output_index]
transfer_input = {'fulfillment': output['condition']['details'],
                  'fulfills': {'output_index': output_index,
                               'transaction_id': transfer_asset['id']},
                  'owners_before': output['public_keys']}

# prepare the transaction and use 3 tokens
prepared_transfer_tx = bdb.transactions.prepare(
    operation='TRANSFER',
    asset=transfer_asset,
    inputs=transfer_input,
    recipients=[([sendr.public_key], 3), ([recvr.public_key], 7)])

# fulfill and send the transaction
fulfilled_transfer_tx = bdb.transactions.fulfill(
    prepared_transfer_tx,
    private_keys=recvr.private_key)
sent_transfer_tx = bdb.transactions.send_commit(fulfilled_transfer_tx)
print(json.dumps(sent_transfer_tx,indent=3))