# '''nums = [7,8,9,10]
# it = iter(nums)

# print(it.__next__())
# print(next(it))'''

# class Topten:
#     def __init__(self):
#         self.num = 1

#     # def __iter__(self):
#     #     return self
    
#     def __next__(self):
#         val = self.num
#         self.num +=1 
#         return val
    
    
# values = Topten()
# print(values.__next__())
# print(values.__next__())
# print(values.__next__())


# class multiples:
#     def __iter__(self):
#         self.val = 1
#         return self
    
#     def __next__(self):
#         temp = self.val
#         self.val +=1
#         return temp*5

# obj = multiples()
# obj1 = iter(obj)

# print(next(obj1))
# print(next(obj1))
# print(next(obj1))
# print(next(obj1))

# def multiple():
#     i=1
#     while True:
#         yield i*5
#         i+=1

# obj = multiple()
# # obj1 = obj
# print(next(obj))
# print(next(obj))
# print(next(obj))

def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@decorator
def greet():
    print("Hello, World!")
greet()