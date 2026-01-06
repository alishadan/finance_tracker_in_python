from datetime import date
import datetime
from pathlib import Path
from transaction import Transaction
from Enter_transaction_functions.get_id import get_id
from Enter_transaction_functions.get_amount import get_amount
from Enter_transaction_functions.get_date import get_date
from Enter_transaction_functions.get_type import get_type
def enter_trans():
    #create a transaction object
     id_tran=get_id()
     amount=get_amount()
     type_amount=get_type()
     date_trans=get_date()
     trans=Transaction(id_tran,amount,type_amount,date_trans)
     return trans




