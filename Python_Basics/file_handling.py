# f = open("demo.txt", "r")
# data = f.read()
# print(data)
# f.close()


# line1 = f.readline()
# print(line1)
# f.close()


# demo file me starting me hello aajega in place of first five letters
# f = open("demo.txt", "r+")
# f.write("hello")
# # hello ke baad se test read krega 
# print(f.read())
# f.close()

# a+ -> at the end pointer ko place krta hai to kuch print nhi hoga 
# f = open("demo.txt", "a+")
# print(f.read())
# f.write("abc")
# f.close()

# def func(file_name):
# file = open("demo.txt", "r", encoding="utf-8")
# for line in file:
#     print(line.strip())

# func("demo.txt")

'''def print_file_with_numbers(file_path):
    f = open(file_path, 'r')
    for num,line in enumerate(f,start=1):
        print(f"{num} : {line.strip()}")

print_file_with_numbers("demo.txt")'''

'''
from collections import Counter
def word_freq(filepath):
    with open("demo.txt",'r') as f:
        return Counter(f.read().split())
    
print(word_freq("demo.txt"))'''

'''import random 
def random_line(filepath):
    with open("demo.txt", 'r') as f:
        f = f.read().splitlines()
        return random.choice(f)
print(random_line("demo.txt"))'''

'''import string, os
store_directory = "letters"
if not os.path.exists(store_directory):
   print("creating directory")
   os.makedirs(store_directory)

for letter in string.ascii_uppercase:
   with open(f"./{store_directory}/{letter}" + ".txt", "w") as f:
       f.writelines(letter) '''

'''
import string, os
store_directory = "letters"
if not os.path.exists(store_directory):
   print("creating directory")
   os.makedirs(store_directory)

with os.scandir(store_directory) as es:
   for e in es:
      if e.is_file() and e.name.endswith('.txt'):
            with open(e.path, 'r') as f:
                print(f.read().strip())
'''

# import string, os

# # if not os.path.exists("letters"):
# #    print("creating directory")
# #    os.makedirs("letters")

# for letter in string.ascii_uppercase:
# #    with open(letter + ".txt", "w") as f:
#          os.remove(letter + ".txt")
#     #    f.writelines(letter) 

'''
with open("demo.txt",'r') as f:
    for line in f:
        print(line)
'''

'''
with open("demo.txt") as f:
    for line in range(5):
        print(f.readline())
'''

'''
import os
 
working_dir = os.getcwd()
 
file_name = "file18.txt"
 
fp = os.path.join(working_dir , file_name)
 
with open(fp,'w') as file:
    file.write("hello")
'''

with open("demo.txt",'r') as f:
    content = f.read().lower()
    