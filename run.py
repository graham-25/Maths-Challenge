# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

print("Hello World")
def checkStock ():
    """
    Function takes a number of stock from the user, checks weather the count is the same as the 
    stock amount and returns the new amount if not. 
    """
    for num in range(10):
        stock_num = 10
        stock_val = int(input("Please enter the count number:"))
        
        if stock_num == stock_val:
            print("Stock number not changed please move on.")
        else:                
            
            print(stock_val)
    

checkStock()
    
       