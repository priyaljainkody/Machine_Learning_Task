
# def storing_line_in_list(f):
#     lst = []
#     f = open("demo.txt", "r")
#     for line in f:
#         lst.append(line.strip())
    
# lines = storing_line_in_list("demo.txt")
# for line in lines:
#     print(line)

"""
lst = []  # Initialize an empty list
with open("demo.txt", "r") as f:  # Open the file in read mode
    for line in f:
        lst.append(line.strip())  # Strip whitespace and append to the list
 
# Print each line from the list
for line in lst:
    print(line)
"""
#write a python program to read first n non empty lines of a file, skipping any blank lines


def non_empty(f):
    non_empty_lines = []
    f = open("demo.txt", "r")
    for line in f:
        stripped_line = line.strip()

        print(len(stripped_line))
        if len(stripped_line) != 0 :
            non_empty_lines.append(stripped_line)
        if len(non_empty_lines) == n:
            break
    print(non_empty_lines)
    return non_empty_lines

n=5
lines=non_empty("demo.txt")
for line in lines:
    print("#########",line)
