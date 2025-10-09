#python that iterate through iterable objects are called interators
"""
nums = [1,2,3,4]
obj = iter(nums)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
"""

#generator -> A generator is a type of function that returns a generator object,
#  which can return a sequence of values instead of a single result. 

"""def nums():
    for i in range(1,9):
        yield(i)

obj = nums()
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))"""

# Iterators are created using classes whereas generators are created using functions.

"""
class Alphabet:
    def __iter__(self):
        self.val = 65
        return self
    
    def __next__(self):
        if self.val>90:
            raise StopIteration
        
        temp = self.val
        self.val += 1
        return chr(temp)

letters = Alphabet()
i1 = iter(letters)
for l in i1:
    print(l, end=" ")
"""

"""
def Alphabet():
    for i in range(65,91):
        yield chr(i)

letters = Alphabet()
for l in letters:
    print(l, end = " ")"""

#Iterators don’t use any variables to iterate whereas generators use local variables
# and store the state of those variables whenever the loop is paused by the yield statement.

"""li = ["A", "B", "C", "D"]
li_iter = iter(li)
print(next(li_iter))
print(next(li_iter))
print(next(li_iter))"""

"""
def gener():
    num = 1
    while True:
        yield num
        num+=1

obj = gener()
print(next(obj))
print(next(obj))
print(next(obj))
"""

#issubclass
"""
from collections.abc import Generator, Iterator
print(issubclass(Iterator,Generator))
print(issubclass(Generator,Iterator))"""

"""
def gener():
    lst = ["orange", "mango", "banana"]
    for i in lst:
        yield(i)

obj = gener()
print(next(obj))
print(next(obj))
print(next(obj))"""

""" LOWER CASE FIRST 3
def abcd():
    for i in range(97,101):
        yield chr(i)

obj = abcd()
print(next(obj))
print(next(obj))
print(next(obj))"""

# multiple of 5 using iterator in class
"""
class multiples:
    def __iter__(self):
        self.val = 1
        return self
    
    def __next__(self):
        temp = self.val
        self.val +=1
        return temp*5

obj = multiples()
obj1 = iter(obj)

print(next(obj1))
print(next(obj1))
print(next(obj1))
print(next(obj1))"""

#multiple of 5 uing function 
def multiple():
    i=1
    while i<=100:
        yield i*5
        i+=1

obj = multiple()
for i in obj:
    print(i)
# print(next(obj))
# print(next(obj))
# print(next(obj))

