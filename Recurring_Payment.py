class RecurringPayment:
    def __init__(self, account, amount, frequency):
        self.account = account
        self.amount = amount
        self.frequency = frequency  # e.g., monthly, weekly

    def process_payment(self):
        self.account.withdraw(self.amount)

