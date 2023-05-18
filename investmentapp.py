import time

profit_percentage = 10

def investment_timer():
    investor_name = "Jack"
    print(investor_name , "Welcome to cohort4 Investment App")
    wallet = 10000
    
    intrest_cal = wallet * profit_percentage / 100
    wallet_balance = wallet + intrest_cal
    print("Dear Investor" , investor_name , "Your Wallet has been credited with the sum of:N" , wallet_balance, "10% interest on your capital")
   
while True:
        investment_timer()
        time.sleep(24 * 60 * 60)