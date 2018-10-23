# this an example of small calculator using function


action = 2

x , y = 4.5 , 3


def addition(num1, num2): # takes two arguments

 return num1 + num2 # return the sum of the two numbers

def substraction(num1, num2):

    
 return num1 - num2 # return the substraction of the two numbers

def multiply(num1, num2):
    
 return num1 * num2 # return the product of the two numbers


def devid(num1, num2):

 return num1 / num2 # return the deivision of the two numbers


if action is 1: # if the value is 1 

 print("The sum is", addition(x,y)) # call the addition function

elif action is 2: # if the above fails, check if the value of action is 2

 print("The difference is", substraction(x,y)) # call the substraction function

elif action is 3: # check for value 3

 print("The product is", multiply(x,y)) # call the multipy function

elif action is 4: # check for a value of 4

 print("The the answer is", devid(x,y)) # call the divistion function

else:

 print("Invalid action, please use an action number between 1 and 4")


