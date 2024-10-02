from account import Account
from random import choice,randint
from log import Log
from unique_transition import UniqueTransition
import threading
class Transition:
    def __init__(self,qnt_transitions:int,type_transition:list) -> None:
        self.value = 0
        self.type_transition = type_transition
        self.qnt_transitions = qnt_transitions
    
    def process_transition(self,account_name:Account):
        id = 0
        log = Log()
        log.create_log()
        for l in range(self.qnt_transitions):
            id +=1
            value_transition = self.value = randint(1,500)
            type_of_transition = choice(self.type_transition)
            account_name.apply_transition(type_of_transition,value_transition)
            transition_request = UniqueTransition(id,value_transition,type_of_transition,account_name.amount)
            log.add_request_log(transition_request)
        log.write_log()
           
            
            
if __name__ == '__main__':
    gabriel = Account()
    transacao_types = ['Crédito','Débito']
    
    transacao = Transition(11000,transacao_types)
    transacao.process_transition(gabriel)
    
    