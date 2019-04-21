## RSA Challenges

Complete the challenges on https://zerodays.ctfd.io and give some detail on each solution.

## Solutions

### Background

These challenges test a person's understanding of the RSA cryptosystem. The letters RSA stand for Rivest–Shamir–Adleman, the authors of the encryption scheme. One of its key features is that it is an assymetric, public key cryptosystem. It has two keys, a public and a private key, where only one of them can decrypt a message encrypted by the other.

### Level 1

![Level 1 screenshot](screenshots/screen-1.png)

We need to encrypt the message "RSA isn't really that hard" and produce the ciphertext as a decimal number. To do this, we must first understand the encryption and decryption processes.

#### RSA Encryption

Given a modulus **n** and a public exponent **e**, to encrypt a message **m**:

`c = m pow e mod n`

Where `c` is the resulting ciphertext, `pow` is exponentiation, and `mod` is modulo.

#### RSA Decryption

Given a modulus **n** and a private exponent **d**, to decrypt a ciphertext **c**:

`m = c pow d mod n`

With this knowledge, all that is left is to convert the given message into a number and encrypt it. The script for the first challenge (solve1.py) does exactly that.

It uses the `binascii` module to convert the message into a hexadecimal string, which is then converted to decimal. Then `pow()` takes the number of the message, raises it to the power of `e` and does modulo `n` to produce the ciphertext value in decimal form.

Result: `13309476856206179288137278795001286676504235122200291222905951541015281640474228799375180129564959032261555135231635439690367282451635413048574322588643043250005501837597608399627442074603517951858976430767446724730937928672932493206869274420288717036712376949408229648116702610597844919828482630797157003777363091998366855062763360538948110895070725322039940644906900772757193759215740687066380017485804644723367158972689710477927318380335919282326398046586751715463059075476044138690978986063001880735783893361380726584661054926968590764176030209214513123458853087059980258593405395678238799024217478961749328706800`

---

### Level 2

![Level 2 screenshot](screenshots/screen-2.png)

### Level 3

![Level 3 screenshot](screenshots/screen-3.png)

### Level 4

![Level 4 screenshot](screenshots/screen-4.png)

### Level 5

![Level 5 screenshot](screenshots/screen-5.png)

### Level 6

![Level 6 screenshot](screenshots/screen-6.png)

### Level 7

![Level 7 screenshot](screenshots/screen-7.png)

### Level 8

![Level 8 screenshot](screenshots/screen-8.png)

### Level 9

![Level 9 screenshot](screenshots/screen-9.png)

### Level 10

![Level 10 screenshot](screenshots/screen-10.png)

### Level 11

![Level 11 screenshot](screenshots/screen-11.png)
