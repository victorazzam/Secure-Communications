#!/usr/bin/env python

from sys import argv

vendors = {
    "American Express" : ([34,37], [15]),
    "Diners Club" : ([300,301,302,303,304,305], [14]),
    "Discover" : ([6011,644,645,646,647,648,649,65] + list(range(622126, 622926)), [16,17,18,19]),
    "InstaPayment" : ([637,638,639], [16]),
    "JCB" : (range(3528, 3590), [16,17,18,19]),
    "Maestro" : ([5018,5020,5038,5893,6304,6759,6761,6762,6763], [16,17,18,19]),
    "MasterCard" : ([51,52,53,54,55] + list(range(222100, 272100)), [16]),
    "Visa" : ([4], [13,16,19])
}

usage = """\nUsage: ccverify <mode> <arg>\nModes:\n
 verify — check if a credit card number is valid
 vendor — print the vendor of a credit card number
 checksum — recover checksum from the first portion of a credit card number
 generate — get a random credit card number for a given vendor\n
Vendors:\n """ + "\n ".join(vendors) + "\n"

luhn = lambda s: sum(int(i) if y % 2 else int(i) * 2 - 9 if int(i) * 2 > 9 else int(i) * 2 for y, i in enumerate(s[-2::-1]))
verify = lambda cc: ("Invalid", "Valid")[not (luhn(cc) + int(cc[-1])) % 10]
check = lambda cc: abs(luhn(cc) % 10 - 10) * (luhn(cc) % 10 > 0)
checksum = lambda cc: check(cc + "0")

def vendor(cc):
    for v in vendors:
        if len(cc) in vendors[v][1] and cc.startswith(tuple(map(str, vendors[v][0]))):
            return v
    return "Unknown vendor."

def generate(v):
    from random import choice
    try:
        cc = str(choice(vendors[v][0]))
        for i in range(choice(vendors[v][1]) - len(cc)):
            cc += str(choice(range(10)))
        return cc[:-1] + str(check(cc))
    except KeyError:
        return f"Vendor '{v}' not recognised."

try:
    exec(f"print({argv[1]}('{argv[2]}'))")
except (NameError, IndexError):
    exit(usage)
except (KeyboardInterrupt, EOFError):
    print()
