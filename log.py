from unique_transition import UniqueTransition
class Log:
    def __init__(self) -> None:
        
        self.list_logs = list()
    
    
    def add_request_log(self,transition:UniqueTransition):
        self.list_logs.append(transition)
        print(f'ID:{transition.id},{transition.type_transition}. Valor:{transition.value}. Saldo restante: {transition.amount_account}')
        