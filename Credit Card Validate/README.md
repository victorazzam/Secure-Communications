## Credit Card Validate

Research the Luhn Formula algorithm used in payment cards and write a program that has the following four modes:

1. **Verify** - determine if a credit card number is valid
2. **Vendor** - output the issuing vendor of a credit card
3. **Checksum** - calculate the checksum from the first portion of a credit card number
4. **Generate** - generate a valid credit card number for a given vendor

## Solution

My program works by taking input via command line arguments. A help page is printed by default, which shows the syntax and available modes, as well as the recognised vendors.

Each mode has its own function, which takes an input and returns a result. If an invalid input or an unknown vendor are given, an error message is returned. The value received from calling the chosen function is printed to the screen.

### Modes

#### Verify

A credit card number is taken as an input. If it contains non-numeric characters, the help page is printed and the program exits. It uses the Luhn Formula algorithm (defined in the function `luhn`) to check if the input is a valid credit card number. It returns "Valid" if the input passes the test, and "Invalid" if it doesn't.

#### Vendor

Given a credit card number, the function iterates through the `vendors` dictionary and tests, for each vendor, if the input abides by the permitted length(s) and starting number(s) for that vendor. If a match is found, the vendor is returned, otherwise "Unknown vendor." is returned.

#### Checksum

Given a credit card number without its last digit (the checksum), the Luhn Formula is used to find the correct checksum, which is then returned. If the input contains non-numeric characters, the help page is printed and the program exits.

#### Generate

The input must be a valid vendor name. It is case-insensitive, so "visa" and "Visa" are seen as equal. The vendor is looked up in the `vendors` dictionary to retrieve its permitted length(s) and starting number(s), and one of each is randomly chosen. The chosen digits are placed at the start of the credit card number, and the rest of the chosen length, except for the last digit, is filled with random numbers from 0 to 9. The last digit is calculated via the Luhn Formula and is appended to the result, producing the final credit card number which is then returned.

### Luhn Formula

The helper function `luhn` implements the Luhn Formula to serve the program's validation functionality. The algorithm follows a series of steps to produce a value, as follows:

1. Take a (credit card) number and remove the last digit, save it for later.
2. Reverse the number.
3. Double all digits in odd positions (index starts at one), subtracting 9 from any result greater than 9.
4. Sum the numbers.
5. Find the number needed to add to the result, in order to reach the next number that is evenly divisble by 10.
6. If the number from step 5 matches the number dropped in step 1, the initial input is a valid credit card number.

A practical example using 123456789 as the input number:

1. 12345678
2. 87654321
3. 77358341
4. 38
5. 2
6. Invalid credit card number, a valid one would be 123456782.
