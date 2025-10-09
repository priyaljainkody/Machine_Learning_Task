import os 
def func(f):
    numbers =0
    f = open("blank.txt" , "r")
    data = f.read()
    numbers = sum([int(word) for word in data.split() if word.isdigit()])
    print(numbers)
    
    y = int(input())    
    try:
        div = numbers/y
        #print(div)
        print(div) #nameError 
    except (ZeroDivisionError, NameError, ValueError) as obj:
        print(obj)
    else:
        print("an exception didn't occur")
    finally: 
        print("always execute")
    print("rest of code")
now = os.getcwd()
print(now)
new = os.path.join(now, 'blankkk1.txt')
print(new)
func("blank.txt")
    
