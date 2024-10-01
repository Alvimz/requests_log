
class Account: 
    def __init__(self) -> None:
        self.amount= 10000
    
    
    def apply_transition(self,transacao):
        self.amount -= transacao.value
    
    def deposit(self,value):
        self.amount+=value
    
    def withdraw(self,value):
        self.amount-=value
        