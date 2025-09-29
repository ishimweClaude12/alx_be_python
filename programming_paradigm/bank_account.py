class BankAccount:
    def __init__(self, initial_balance: float = 0.0):
        """Initialize a bank account with an optional starting balance."""
        self.__account_balance = initial_balance  # encapsulated attribute

    def deposit(self, amount: float) -> None:
        """Deposit a positive amount into the account."""
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.__account_balance += amount

    def withdraw(self, amount: float) -> bool:
        """Withdraw amount if sufficient funds are available."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self) -> None:
        """Display the current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
