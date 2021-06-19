# week4
Cash Register Program 

Current Issue: how to calculate daily sales? Below are the options I'm pursuing. 
1) Use values from dictionary (transaction_dict)
2) Create a separate list (sales_for_day)

So this was quite a challenging exercise. I started with the file cash_register.py. I could not figure out how to approach this problem, but after messing around with a couple of functions and loops, I then went to pen and paper. The way I conceptualized it was this: there is a main program (cash register) which is comprised of three functions (or sub programs) which will continue running unless the sub program/function, 'exit', is run. 
Main Program: cash_register.py
Function 1: New Transaction
Function 2: Current Transactions
Function 3: Exit 

I then tried to start developing the main program in the file cash_register_notes.py. This file was quickly discarded from my work flow but I did gain the insight that I needed a while-loop (maybe I didn't 'need' a while loop, but it's what i came up with)

Having never used the dictionary data type, i had to spend a decent bit of time figuring out how use it online. Evidence of this tinkering around can be found in the file append_dictionary_transaction.py. 

After I figured out how to add items to a dictionary, I began working on the file transaction_function.py. This went relatively smoothly as I just kept adding a line or two, running/debugging, and repeated. I then added this information into the main program (cash_register.py) and began building the overall program. At this point, i think it works well minus the issue stated up front. 
