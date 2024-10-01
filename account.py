
class Account: 
    def __init__(self) -> None:
        self.amount= 10000
    
    #getter and setter here
    
    def apply_transition(self,transacao:str):
        match transacao:
            case 'Crédito':
                self.deposit()
            case 'Débito':
                self.withdraw()
                
                
            
    
    def deposit(self,value):
        self.amount+=value
    
    def withdraw(self,value):
        self.amount-=value
        