from User import User

class Admin:
    def __init__(self, email_id, name):
        self.email_id = email_id
        self.name = name
        self.users = []
        self.total_loan_amount = 0
        self.loan_feature_on = True

    def create_user_account(self, email_id, name, password, initial_dep=0):
        user = User(email_id, name, password, initial_dep)
        self.users.append(user)
        return user

    def check_total_balance(self):
        return sum(user.balance for user in self.users)

    def check_total_loan_amount(self):
        return sum(user.loan for user in self.users)

    def toggle_loan_feature(self, status):
        self.loan_feature_on = status

# Example usage
admin = Admin("admin@example.com", "Admin")

# Admin creates user accounts
user1 = admin.create_user_account("user1@com", "sakib", "password1", 1000)
user2 = admin.create_user_account("user2@gmail.com", "Natasha", "password2", 500)

# User creates his own account
user3 = User("bab@g", "shahman", "pass3", 3000)
user3.create_own()

# User actions
print(user1.deposite(500))  # Here User1 deposits tk 500
print(user1.withdrawl(300))  # User1 withdraws tk 300
print(user1.transfer(user2, 200))  # User1 transfers tk 200 to User2
print(user1.check_balance())  # User1 checks balance
print(user1.take_loan(2000))  # User1 takes a loan
print(user1.check_transaction_history())  # User1 checks transaction history

# Admin actions
print(admin.check_total_balance())  # Admin checks total balance
print(admin.check_total_loan_amount())  # Admin checks total loan amount
admin.toggle_loan_feature(False)  # Admin disables loan feature
