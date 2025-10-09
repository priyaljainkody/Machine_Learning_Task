def line_count(file_path):
    f = open("demo.txt", "r")
    count_number = 0
    while(f.readline()):
        count_number+=1
    print(count_number)

def count_char(file_path):
    f = open("demo.txt", "r")
    for line_number, line in enumerate(f, start=1):
        print(f"line {line_number} : {len(line.strip())} characters")

def count_word(file_path):
    f = open("demo.txt", "r")
    for line_number, line in enumerate(f, start=1):
        print(f"line {line_number} : {len(line.split())} words")

line_count("demo.txt")
count_char("demo.txt")
count_word("demo.txt")