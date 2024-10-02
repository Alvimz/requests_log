class Account: 
    def __init__(self) -> None:
        self._amount= 10000
    
    #getter and setter here
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self,value):
        if value < 0:
            raise ValueError('Saldo insuficiente para transação!')
        self._amount = value
            
    
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
        