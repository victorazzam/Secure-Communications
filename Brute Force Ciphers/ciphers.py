#!/usr/bin/env python3

from sys import argv

charsets = {
    "dec": "Digits",
    "alpha": "Letters, uppercase and lowercase",
    "all": "All printable characters"
}

def rot_dec(s):
    for rot in range(-5, 5):
        print("".join(str((int(c) + rot) % 10) if c.isdigit() else c for c in s))

def rot_alpha(s):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = upper.lower()
    for rot in range(26):
        out = ""
        for c in s:
            if c in upper:
                c = upper[(upper.find(c) + rot) % 26]
            elif c in lower:
                c = lower[(lower.find(c) + rot) % 26]
            out += c
        print(out)

def rot_all(s):
    chars = list(map(chr, range(33, 127)))
    for rot in range(94):
        print("".join(chars[(chars.index(c) + rot) % 94] if c in chars else c for c in s))

def main():
    if len(argv) != 3 or argv[1] not in charsets:
        print(f"\nString Rotations Generator\n\nUsage: {argv[0]} charset text\n\nCharsets: ", end="")
        exit(f'\n{"":10}'.join(f"{k:6}- {v}" for k,v in charsets.items()) + "\n")
    exec(f"rot_{argv[1]}({repr(argv[2])})")

if __name__ == "__main__":
    main()
