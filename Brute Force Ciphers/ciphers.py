#!/usr/bin/env python3

from sys import argv

charsets = {
 "dec": ("digits", (48, 58)),
 "alpha": ("letters, uppercase and lowercase", (65, 91), (97, str.islower)),
 "all": ("all printable characters", (33, 127))
}

def rotate(s, r, alt=None):
    base = len(list(range(*r)))
    for rot in range(base):
        print(rot, end=". ")
        out = ""
        for c in s:
            start = alt[0] if alt[1](c) else r[0]
            if ord(c) - start in range(base):
                out += chr((ord(c) + rot - start) % base + start)
            else:
                out += c
        print(out)

try:
    if len(argv) != 3 or argv[1] not in charsets:
        print(f"\nString Rotations Generator\n\nUsage: {argv[0]} charset text\n\nCharsets: ", end="")
        exit(f'\n{"":10}'.join(f"{k:6}- {v[0]}" for k, v in charsets.items()) + "\n")
    rotate(argv[2], *charsets[argv[1]][1:])
except (KeyboardInterrupt, EOFError):
    print()
