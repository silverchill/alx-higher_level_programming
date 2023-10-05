#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
sum = 0
for w in range(len(argv[1:])):
    sum += int(argv[w + 1])

print(sum)
