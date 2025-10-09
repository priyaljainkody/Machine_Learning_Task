def lines(f,specific_word):
    f = open("demo.txt", "r")
    for line in f:
        if specific_word in line:
            print(line.strip())

lines("demo.txt", "you")
