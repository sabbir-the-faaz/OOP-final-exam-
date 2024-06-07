class User:
    def __init__(self, email_id, name, password, initial_dep=0) -> None:
        self.email_id = email_id
        self.name = name
        self.password = password
        self.balance = initial_dep
        self.loan = 0
        self.transac_his = []

    def create_own(self):
        print(f'Thank you {self.name} for creating an account')

    def deposite(self, amount):
        self.balance += amount
        self.transac_his.append(f'yo! We have deposited {amount} into your account')
        return self.balance

    def withdrawl(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transac_his.append(f'You have withdrawn {amount} from your account')
            return self.balance
        else:
            return "The bank is bankrupt. Tomar tk nai"

    def check_balance(self):
        return self.balance

    def transfer(self, receiver, amount):
        if amount <= self.balance:
            self.balance -= amount
            receiver.balance += amount
            self.transac_his.append(f'Transferred {amount} from your account')
            receiver.transac_his.append(f'Received {amount} from {self.name}')
            return self.balance
        else:
            return "Not enough tk"

    def check_transaction_history(self):
        return self.transac_his

    def take_loan(self, loan_amount):
        if loan_amount <= 2 * self.balance and self.loan == 0:
            self.balance += loan_amount
            self.loan += loan_amount
            self.transac_his.append(f'Loan taken {loan_amount} for your account')
            return self.balance
        else:
            return "Loan request denied"

# Example user creation
user3 = User("user3@gmail.com", "Rakib", "password3", 2000)
user3.create_own()
