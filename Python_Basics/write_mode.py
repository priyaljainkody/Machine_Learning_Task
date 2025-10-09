# To overwrite the content of a file or create a new file if it doesn’t exist, 
# use the 'w' mode (write mode)

def func(f):
    f = open("demo1.txt", 'w')
    f.write("this write mode overwrite the text")

func("demo1.txt")

