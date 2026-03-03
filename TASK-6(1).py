class BankAccount:
    """A base class to represent a generic bank account."""
    def __init__(self, account_number, initial_balance=0.0):
        self._account_number = account_number # Encapsulated account number
        self._balance = initial_balance # Encapsulated balance
    def deposit(self, amount):
        """Deposits funds into the account."""
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        """Withdraws funds from the account, subject to balance check."""
        if amount > 0:
            if self._balance >= amount:
                self._balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self._balance}")
                return True
            else:
                print("Insufficient funds.")
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False
    def get_balance(self):
        """Returns the current account balance."""
        return self._balance
    def get_account_number(self):
        """Returns the account number."""
        return self._account_number
    def __str__(self):
        return f"Account #{self._account_number}, Balance: ${self._balance:.2f}"
class SavingsAccount(BankAccount):
    """A savings account with an interest rate and interest calculation."""
    def __init__(self, account_number, initial_balance=0.0, interest_rate=0.01):
        super().__init__(account_number, initial_balance)
        self._interest_rate = interest_rate # Encapsulated interest rate
    def calculate_interest(self):
        """Calculates and deposits interest into the account."""
        interest = self._balance * self._interest_rate
        if interest > 0:
            self.deposit(interest)
            print(f"Interest of ${interest:.2f} added at a rate of {self._interest_rate*100}%")
    def __str__(self):
        return f"Savings Account #{self._account_number}, Balance: ${self._balance:.2f}, Rate: {self._interest_rate*100}%"
class CurrentAccount(BankAccount):
    """A current account with a minimum balance requirement."""
    def __init__(self, account_number, initial_balance=0.0, minimum_balance=500.0):
        # Ensure initial balance meets minimum requirement if it's set higher than 0.0
        if initial_balance < minimum_balance:
             print(f"Warning: Initial balance ${initial_balance} is below minimum requirement of ${minimum_balance}.")
        super().__init__(account_number, initial_balance)
        self._minimum_balance = minimum_balance # Encapsulated minimum balance
    def withdraw(self, amount):
        """Withdraws funds, ensuring the balance does not drop below the minimum."""
        if amount > 0:
            if self._balance - amount >= self._minimum_balance:
                # Use the parent class's withdraw logic after the check
                return super().withdraw(amount)
            else:
                print(f"Withdrawal failed. Balance cannot fall below the minimum of ${self._minimum_balance}.")
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False
    def __str__(self):
        return f"Current Account #{self._account_number}, Balance: ${self._balance:.2f}, Min Balance: ${self._minimum_balance:.2f}"
# Create a Savings Account
savings = SavingsAccount(account_number="S123", initial_balance=1000, interest_rate=0.02)
print(savings)
# Deposit and withdraw from Savings Account
savings.deposit(200)
savings.withdraw(500)
savings.withdraw(1000) # Fails due to insufficient funds
# Calculate interest for Savings Account
savings.calculate_interest()
print(savings.get_balance())
# Create a Current Account
current = CurrentAccount(account_number="C456", initial_balance=2000, minimum_balance=500)
print(current)
# Deposit and withdraw from Current Account
current.deposit(100)
current.withdraw(1400) # Fails because balance would drop to 700 (below min of 500)
current.withdraw(1000) # Succeeds
print(current)
