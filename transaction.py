from datetime import datetime
class Transaction:
    def __init__(self,id_trans,amount,type_amount,date_trans):
        self.id=id_trans
        self.amount=amount
        self.type_trans=type_amount
        self.date_trans=date_trans
    def to_dict(self):
        return {
                "id":self.id,
                "amount":self.amount,
                "type":self.type_trans,
                "date":self.date_trans.isoformat()
            }
    @classmethod
    def from_dict(cls,data):
        return cls(
            id_trans=data["id"],
            amount=data["amount"],
            type_amount= data["type"],
            date_trans=datetime.fromisoformat(data["date"]) 
        )




