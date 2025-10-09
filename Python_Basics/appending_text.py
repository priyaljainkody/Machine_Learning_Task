# To add content to an existing file without overwriting its current content,
#  use the 'a' mode (append mode):
def func(f):
    f = open("demo.txt", "a")
    f.write("python programming")
    
func("demo.txt")

