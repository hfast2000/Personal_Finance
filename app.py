from account import Account
from Recurring_Payment import RecurringPayment
from Visualizations import plot_pie_chart, plot_income_vs_expense



def display_menu():
    print("\nWelcome to the Personal Finance Tracker!")
    print("1. Add Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Set Account Goal")
    print("5. View Account Visualizations")
    print("6. Process Recurring Payments")
    print("7. Exit")

def main():
    accounts = []
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':  # Add Account
            print("The following accounts are already active:")
            for i in accounts:
                print(f"- {i.name} (Balance: ${i.balance:.2f})")
            name = input("Enter account name: ")
            balance = float(input("Enter starting balance: "))
            account = Account(name, balance)
            accounts.append(account)
            print(f"Account {name} added successfully!")

        elif choice == '2':  # Deposit Money
            print("Pick from one of the following accounts:")
            for i in accounts:
                print(f"- {i.name} (Balance: ${i.balance:.2f})")
            name = input("Enter account name: ")
            amount = float(input("Enter amount to deposit: "))
            for account in accounts:
                if account.name == name:
                    account.deposit(amount)
                    print(f"{amount} deposited into {name}")
                    break
            else:
                print("Account not found.")

        elif choice == '3':  # Withdraw Money
            print("Pick from one of the following accounts:")
            for i in accounts:
                print(f"- {i.name} (Balance: ${i.balance:.2f})")
            name = input("Enter account name: ")
            amount = float(input("Enter amount to withdraw: "))
            for account in accounts:
                if account.name == name:
                    account.withdraw(amount)
                    print(f"{amount} withdrawn from {name}")
                    break
            else:
                print("Account not found.")

        elif choice == '4':  # Set Account Goal
            print("Pick from one of the following accounts:")
            for i in accounts:
                print(f"- {i.name} (Balance: ${i.balance:.2f})")
            name = input("Enter account name: ")
            goal = float(input("Enter goal amount: "))
            for account in accounts:
                if account.name == name:
                    account.set_goal(goal)
                    print(f"Goal of {goal} set for {name}")
                    break
            else:
                print("Account not found.")

        elif choice == '5':  # View Account Balances (Pie Chart)
            print("What kind of data would you like to see:")
            print("1. Pie Chart of all accounts")   
            print("2. Income vs. Expenses bar graph" )
            visual_choice = int(input("Choose an option: "))
            if visual_choice == 1:
                plot_pie_chart(accounts)
            elif visual_choice == 2:
                plot_income_vs_expense(accounts)

        elif choice == '6':  # Process Recurring Payments
            print("Pick from one of the following accounts:")
            for i in accounts:
                print(f"- {i.name} (Balance: ${i.balance:.2f})")
            name = input("Enter account name for recurring payment: ")
            amount = float(input("Enter recurring payment amount: "))
            frequency = input("Enter payment frequency (e.g., monthly): ")
            for account in accounts:
                if account.name == name:
                    recurring_payment = RecurringPayment(account, amount, frequency)
                    recurring_payment.process_payment()
                    print(f"Processed {frequency} payment of {amount} from {name}")
                    break
            else:
                print("Account not found.")

        elif choice == '7':  # Exit
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

