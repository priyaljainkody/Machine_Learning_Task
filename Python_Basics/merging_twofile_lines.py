'''with open("demo.txt") as fh1, open("demo1.txt") as fh2:
    for line1,line2 in zip(fh1,fh2):
        print(line1+line2)'''

def longest_word(filepath):
    with open("demo.txt","r") as f:
        words = f.read().split()
    max_len = len(max(words, key = len))
    return set([word for word in words if len(word) == max_len])

print(longest_word("demo.txt"))