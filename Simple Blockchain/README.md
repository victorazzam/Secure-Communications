## Simple Blockchain

Some online service uses hash chains. Given the user nOOB and its seed 654e1c2ac6312d8c6441282f155c8ce9, find out how to authenticate as the user ECSC for the given challenge hash c89aa2ffb9edcc6604005196b5f0e0e4. The string, or hash, that hashes to this hash, is the solution.

## Solution

The first step in impersonating a user is to get their seed. The seed is the first string that gets hashed, which then continually gets hashed to form a chain of hashes known as a hash chain.

To find out the seed of the user ECSC, it is important to understand how the seed for the user nOOB is generated. I used [crackstation.net](https://crackstation.net) to see if the seed for nOOB is a known hash, and indeed so - it is generated from MD5 hashing the username with inverted case (uppercase letters become lowercase and vice versa).

So nOOB becomes Noob and then the MD5 hash of that is the hash chain seed. Likewise, ECSC becomes ecsc and its MD5 hash is the seed. Now all that is left is to keep hashing "ecsc" until right before the challenge hash is reached. The hash before c89aa2ffb9edcc6604005196b5f0e0e4 in the chain is the desired result.

In my code, I import the hashlib module and initialise two strings:

1. `chain` is the value to be continually hashed
2. `target` specifies where stop hashing in order to get the required result

Then a while loop keeps MD5 hashing `chain` and testing if its next value is equal to `target` and, if so, it quits the loop and prints the value of `chain`.

The output after running the script is `6fe9b4d366668a1f8a964a72cbc912c8` which is the hash that, when MD5 hashed, produces the challenge hash.
