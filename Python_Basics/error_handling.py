'''
try:
      # Code that might raise an exception
except SomeException:
      # Code to handle the exception
else:
     # Code to run if no exception occurs
finally:
    # Code to run regardless of whether an exception occurs
'''

'''
num1 = int(input())
num2 = int(input())

try:
    div = num1/num2
    #print(div)
    print(div) #nameError 
except (ZeroDivisionError, NameError, ValueError) as obj:
    print(obj)
else:
    print("an exception didn't occur")
finally: 
    print("always execute")
print("rest of code")

'''
try:
    x = int("str")  # This will cause ValueError
    
    #inverse
    inv = 1 / x
    
except (ValueError,ZeroDivisionError) as obj:
    print(obj)
