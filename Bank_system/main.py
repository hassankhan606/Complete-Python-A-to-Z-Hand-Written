def main_menu():
    print("\n🏦 Welcome to Python Bank System")
    print("1. Admin Login")
    print("2. Customer Login")
    print("3. Exit")

# * Admin Login
def admin_login():
    username = input("Enter Admin Username: ")
    password = input("Enter Admin Password: ")

    if username == "Hassan" and password == "123":
        print("✅ Admin login successful!")
        admin_menu()  # Go to admin menu after login
    else:
        print("❌ Login failed! Invalid credentials.")

# * Admin Menu
def admin_menu():
    while True:
        print("\n🔧 Admin Menu")
        print("1. Create New Account")
        print("2. View All Accounts")
        print("3. Back to Main Menu")
        choice = input("Enter choice: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            view_all_accounts()
        elif choice == '3':
            break
        else:
            print("❗Invalid choice.")

# * Create Account
def create_account():
    account_no = input("Enter the Account Number: ")
    name = input("Enter Customer Name: ")
    password = input("Set a Password: ")
    balance = input("Enter Initial Balance: ")

    with open("accounts.txt", "a") as f:
        f.write(f"{account_no},{name},{password},{balance}\n")
    
    print("✅ Account created successfully!")

# * View All Accounts
def view_all_accounts():
    print("\n📄 All Accounts")
    try:
        with open("accounts.txt", 'r') as f:
            for line in f:
                data = line.strip().split(",")
                if len(data) >= 4:
                    account_no, name, _, balance = data
                    print(f"Account No: {account_no} | Name: {name} | Balance: Rs{balance}")
    except FileNotFoundError:
        print("⚠️ No accounts found.")

# * Customer Login
def customer_login():
    account_no = input("Enter Account Number: ")
    password = input("Enter Password: ")

    found = False
    try:
        with open("accounts.txt", "r") as f:
            for line in f:
                data = line.strip().split(",")
                if len(data) >= 3 and data[0] == account_no and data[2] == password:
                    print(f"✅ Welcome, {data[1]}!")
                    found = True
                    break
        if not found:
            print("❌ Account not found or wrong password.")
    except FileNotFoundError:
        print("⚠️ No accounts found. Please ask admin to create one.")

# * Program Execution Starts Here
while True:
    main_menu()
    choice = input("Enter Your Choice (1-3): ")

    if choice == '1':
        admin_login()
    elif choice == '2':
        customer_login()
    elif choice == '3':
        print("👋 Thank you for using Python Bank System!")
        break
    else:
        print("❗Invalid choice. Please try again.")

# * Customer Menu
def customer_menu(account_no):
    while True:
        print("\n💼 Customer Menu")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            deposit_money(account_no)
        elif choice == '2':
            withdraw_money(account_no)
        elif choice =='3': 
            check_balance(account_no)
        elif choice == '4':
            break
        else:
            print("❗Invalid choice.")                 
            
def deposit_money(account_no):
    amount = float(input("Enter amount to deposit: "))
    lines = []
    updated = False

    with open("accounts.txt", "r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] == account_no:
                data[3] = str(float(data[3]) + amount)
                updated = True
            lines.append(",".join(data))

    if updated:
        with open("accounts.txt", "w") as f:
            for line in lines:
                f.write(line + "\n")
        print(f"✅ Rs {amount} deposited successfully.")
    else:
        print("❌ Account not found.")


def withdraw_money(account_no):
    amount = float(input("Enter amount to withdraw: "))
    lines = []
    updated = False

    with open("accounts.txt", "r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] == account_no:
                if float(data[3]) >= amount:
                    data[3] = str(float(data[3]) - amount)
                    updated = True
                else:
                    print("❌ Not enough balance.")
                    return
            lines.append(",".join(data))

    if updated:
        with open("accounts.txt", "w") as f:
            for line in lines:
                f.write(line + "\n")
        print(f"✅ Rs {amount} withdrawn successfully.")
    else:
        print("❌ Account not found.")

def check_balance(account_no):
    with open("accounts.txt", "r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] == account_no:
                print(f"💰 Current Balance: Rs {data[3]}")
                return
    print("❌ Account not found.")
          