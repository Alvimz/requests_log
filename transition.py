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
            self.value = randint(1,500)
            currenty_type = choice(self.type_transition)
            if self.type_transition == 'Crédito':
                account_name.amount+= self.value
            else:
                if account_name.amount<self.value:
                    return 'Transação inválida!'
                account_name.amount-= self.value
            self.transition_log(f'ID:{self.id}, Transação no valor de {self.value} do tipo {currenty_type}')
        return account_name
            
    def transition_log(self,transition):
        self.transition_list.append(transition)
        return self.transition_list
        
        
        
            
if __name__ == '__main__':
    gabriel = Account()
    transacao_types = ['Crédito','Débito']
    
    transacao = Transition(100,transacao_types)
    
    transacao.process_transition(gabriel)
    for transition in transacao.transition_list:
        print(transition)
    print(f'Saldo da conta: {gabriel.amount}')
    