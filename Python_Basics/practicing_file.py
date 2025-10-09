#f = open("myfile.txt", "x") #Create a new file called "myfile.txt"

''' 
import os 
print(os.getcwd()) #current working directory 
os.chdir('c:\\helloo') #change current working directory
print(os.getcwd())
'''

#os.mkdir("newfolder") #create single folder in current directory 

#os.makedirs("one/two") #makes multiple folder in current directory 

#os.rmdir("newfolder") #it removes single folder 

#os.removedirs("one/two")

'''
print(os.listdir())  # or you can write ---> print(os.listdir('.')) 

print(os.listdir('c:\\'))

print(os.path.exists("c:\\helloo\\one"))
print(os.path.exists("c:\\helloo\\abc"))

'''
import os
now = os.getcwd()
print(now)
new = os.path.join(now, 'blank.txt')
f = open(new, 'w')
f.close()