#****************TASK 1***********************
#**************The Smart ATM******************
#*********************************************


initial_balance=5000 #Initial account balance
withdrawal=1350 #The amount to withdraw

balance=initial_balance-withdrawal #Calculating balance

print("The initial balance:",initial_balance) # Displaying initial account balance
print("The amount to withdraw:",withdrawal) # The amount to withdraw
print("The balance amount:",balance) # The remaining balance
print("Is withdrawal amount less than available balance:", initial_balance<withdrawal)  #checking withdrawal possible
print("Is remaining balance greater than 1,000:",balance>1000) #checking remaining balance greater than 1000
print("500 notes needed for the remaining balance:",balance//500,"and remaining amount needed:",balance%500) #Calculating the no. of 500 notes needed and reamining amount