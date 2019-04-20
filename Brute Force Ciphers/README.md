## Brute Force Ciphers

The task is to create a script that shows all the character rotations of a particular string, in three different modes:

1. Decimal, for digits (rot5)
2. Alphabetical, for letters (rot13)
3. All printable ASCII characters (rot47)

## Solution

My script for this lab uses one function to do all the rotations. It accepts arguments provided on the command line. If incorrect arguments are given, the program prints some helpful syntax and options information.

The function `rotate()` is called with the input text and the chosen character set's corresponding ASCII range, as well as a possible alternative starting point in the ASCII range. The alternative serves as a way to allow the differentiation of lowercase and uppercase letters, but could be used to test other conditions too.

In `rotate()` the base is calculated from the ASCII range provided. Then each rotation in the range is iterated through and the rotation number is printed. Every letter from the input is summed with the rotation number, and overflowing values are brought back to the start of the range. At the end of a rotation, the result is printed and the cycle continues, until the range has been exhausted.

Since rotations start at zero, the first line will always print the user-supplied string. If an `alt` is specified, its condition is used to determine if a different starting point of the ASCII range is to be chosen; the base will remain the same, so lowercase letters can be rotated separately from uppercase ones.

Lastly, if any characters do not appear in a given range, they are printed as-is.
