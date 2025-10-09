def replace_substring_occurrence(f):
    f = open("demo.txt","r")
    string = f.read()
    replace_string = string.replace("can","may")
    print(replace_string)

replace_substring_occurrence("demo.txt")