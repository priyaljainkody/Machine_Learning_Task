def reverse_file_lines(f):
    f = open("demo.txt", "r")
    for line in f:
        reverse_lines = "".join(line.split()[::-1])
        print(reverse_lines)

reverse_file_lines("demo.txt")

