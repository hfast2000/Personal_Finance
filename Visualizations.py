import matplotlib.pyplot as plt

def plot_pie_chart(accounts):
    account_names = [account.name for account in accounts]
    balances = [account.balance for account in accounts]
    plt.pie(balances, labels=account_names, autopct='%1.1f%%', startangle=90)
    plt.title("Account Balances")
    plt.show()

def plot_income_vs_expense(accounts):
    # For simplicity, just plot a basic bar graph of balances
    account_names = [account.name for account in accounts]
    balances = [account.balance for account in accounts]

    plt.bar(account_names, balances, color='skyblue')
    plt.xlabel("Accounts")
    plt.ylabel("Balance")
    plt.title("Account Balances Overview")
    plt.show()

