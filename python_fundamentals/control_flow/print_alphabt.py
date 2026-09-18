#!/usr/bin/env python3
result = ""
for i in range(ord('a'), ord('z') + 1):
    if (i == ord('q') or i == ord('e')):
        continue
    result += chr(i)
print(result)