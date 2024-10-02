from account import Account
from random import choice,randint


class Transition:
    def __init__(self,qnt_transitions:int,type_transition:list) -> None:
        self.id = 0
        self.value = 0
        self.type_transition = type_transition
        self.qnt_transitions = qnt_transitions
        self.transition_list = list()
        
    
    def process_transition(self,account_name:Account):
        for l in range(self.qnt_transitions):
            self.id +=1
            value_transition = self.value = randint(1,500)
            type_of_transition = choice(self.type_transition)
            account_name.apply_transition(type_of_transition,value_transition)
            self.transition_log((self.id,account_name.amount,type_of_transition,value_transition,))
           
            
            
    def transition_log(self,transition):
        self.transition_list.append(transition)
        return self.transition_list
        
        
        
            
if __name__ == '__main__':
    gabriel = Account()
    transacao_types = ['Crédito','Débito']
    
    transacao = Transition(3,transacao_types)
    
    transacao.process_transition(gabriel)
    print(transacao.transition_list)
    
    print(f'Saldo da conta: {gabriel.amount}')
    