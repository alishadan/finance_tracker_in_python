import json
import os
import json
from transaction import Transaction

def save_data(trans: Transaction):
    with open("trans.jsonl", "a") as file:
        file.write(json.dumps(trans.to_dict()) + "\n")


