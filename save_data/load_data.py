import json
import os
from transaction import Transaction
def load_data():
    if os.path.isfile("trans.jsonl") and os.path.getsize("trans.jsonl")>0:
        transactions=[]
        with open("trans.jsonl","r") as file:
         for line in file:
             data=json.loads(line)
             transactions.append(Transaction.from_dict(data))
         return transactions
    else:
        print("file trans.jsonl not exsist")

def stream_data():
    if os.path.isfile("trans.jsonl") and os.path.getsize("trans.jsonl")>0:
        with open("trans.jsonl","r",encoding="utf-8") as file:
           for line in file:
                data=json.loads(line)
                yield Transaction.from_dict(data)
    else:
        print("trans.jsonl dont exist \n")
