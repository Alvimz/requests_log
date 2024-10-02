class Account: 
    def __init__(self) -> None:
        self.amount= 10000
    
    #getter and setter here
    
    def apply_transition(self,type_transition,value):
        match type_transition:
            case 'Crédito':
                return self.deposit(value)
            case 'Débito':
                return self.withdraw(value)
                
                
            
    
    def deposit(self,value):
        self.amount+=value
        
    
    def withdraw(self,value):
        self.amount-=value
        