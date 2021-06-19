
#Create dictionary for transaction list
transaction_dict = {}

cashier_choice = input("[1] Start new transaction \n[2] Current running transactions \n[3] Exit" )

#probably should use a while-loop to control: i.e., while cashier_choice != 3: 
if cashier_choice == "1":
    print("~~~Starting New Transaction")
elif cashier_choice == "2":
    print("~~~Here are the current transactions")
elif cashier_choice == "3":
    print("WOO HOO! Day is over~~~")
    print("Great Job Today:")
    print("Transactions:", len(transaction_dict))
    print("Total sales:")
    print("")
    print("~~~GOODBYE~~~")
else:
    print()