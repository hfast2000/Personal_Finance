class Account:
    def __init__(self, name, balance=0, goal=None):
        self.name = name
        self.balance = balance
        self.goal = goal

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def set_goal(self, goal_amount):
        self.goal = goal_amount
