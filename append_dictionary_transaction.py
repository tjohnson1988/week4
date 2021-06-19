item_tuple = (4.5, 1.5, 1.0)
transaction_dict = {}

transaction_number = 1
total_amount = 0
total_amount += item_tuple[2] 
payment_method = "Credit"
print(total_amount)
transaction_dict[transaction_number] = str(total_amount), payment_method
print(transaction_dict)
print(len(transaction_dict))

#def new_transaction():
#    transaction_total = 0.0 
#    user_choice = input("Choose (1) Hotdog, (2) Soda, or (3) Chips")
#    if user_choice == "1":
#        transaction_total = transaction_total + float(item_tuple[1])

#new_transaction()

#transaction_dict['transaction_number'] = transaction_total

