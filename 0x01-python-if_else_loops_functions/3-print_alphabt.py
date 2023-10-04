#!/usr/bin/python3
for w in range(ord('a'), ord('z') + 1):
    if chr(w) == 'q' or chr(w) == 'e':
        continue
    print('{:c}'.format(w), end='')
