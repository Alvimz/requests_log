from unique_transition import UniqueTransition
import os
from datetime import datetime
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
        return self.list_logs
    
    def write_log(self):
        for item in self.list_logs:
            time_now = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            with open('log.txt','a',encoding='utf-8') as f:
                f.write(f'[{time_now}] ID:{item.id} - Transação {item.type_transition} - Valor:R${item.value} - Saldo: R${item.amount_account}\n')