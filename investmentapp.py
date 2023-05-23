import time
import datetime 

profit_percentage = 10

#def investment_timer():
investor_name = input('Enter Name')
print(investor_name , "Welcome to cohort4 Investment App")
wallet = int(input('Enter amount'))
transaction_time = datetime.datetime.now()

while True:
    profit = wallet * profit_percentage/ 100
    Wallet += profit
    text = '{} Your account has been credited with sum of :N {:,.2f} with a 10% profit on your capital at : "{}'
    print(text.format(investor_name , wallet,transaction_time))
    


    time.sleep(24*60*60)
    
 