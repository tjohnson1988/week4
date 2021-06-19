#tuple of items for sale
items_for_sale = (4.5, 1.5, 1.0)

#dictionary of transactions {1 (transaction number) :['$' (total order), 'Credit' (type of payment)]}
transaction_dict = {}

#transaction counter used for giving key values to dictionary of transaction
transaction_number = 1 

def new_transaction():
    print("~~~Starting New Transaction~~~")
    basket = 0
    transaction_input = 0
    while transaction_input != "4":
        transaction_input = input(" [1] - Hot Dog - $4.50 \n [2] - Soda - $1.50 \n [3] - Chips - $1.00 \n [4] - Start Payment Process \n")
        if transaction_input == "1":
            print("~~ You added a hot dog ~~")
            basket += float(items_for_sale[0])
            print("Your current total is:", basket)        
        elif transaction_input =="2":
            print("~~ You added a soda ~~")
            basket += float(items_for_sale[1])
            print("Your current total is:", basket)
        elif transaction_input =="2":
            print("~~ You added chips ~~")
            basket += float(items_for_sale[2])
            print("Your current total is:", basket)
    print("Your total is: $", basket)
    payment_method = input("How would you like to pay? \n [1]Cash \n [2]Credit \n")
    if payment_method == "1":
        print("~~ You have selected cash")
        payment_method = "Cash"
    elif payment_method == "2":
        print("~~ You have selected credit ~~")
        payment_method = "Credit"
    print("~~ Thank you for choosing Wally's! ~~")
    transaction_dict[transaction_number] = str(basket), payment_method
    print(transaction_dict)
    
    
new_transaction()