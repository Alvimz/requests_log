from unique_transition import UniqueTransition
import os
class Log:
    def __init__(self) -> None:
        self.list_logs = list()
        self.create_log()
    
    @staticmethod
    def create_log():
        if not os.path.exists('./log.txt'):
            with open('log.txt','w') as f:
                ...
    
    def add_request_log(self,transition:UniqueTransition):
        self.list_logs.append(transition)
        print(f'ID:{transition.id},{transition.type_transition}. Valor:{transition.value}. Saldo restante: {transition.amount_account}')
        