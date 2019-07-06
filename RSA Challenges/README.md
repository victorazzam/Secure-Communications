## RSA Challenges

Complete the challenges on https://zerodays.ctfd.io and give some detail on each solution.

## Solutions

### Background

These challenges test a person's understanding of the RSA cryptosystem. The letters RSA stand for Rivest–Shamir–Adleman, the authors of the encryption scheme. One of its key features is that it is an assymetric, public key cryptosystem. It has two keys, a public and a private key, where only one of them can decrypt a message encrypted by the other.

---

### Level 1

![Level 1 screenshot](screenshots/screen-1.png)

We need to encrypt the message `RSA isn't really that hard` and produce the ciphertext as a decimal number. To do this, we must first understand the encryption and decryption processes.

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

The task is to decrypt the given ciphertext using the values from the first challenge. We know that decryption can be done using `d` and `n`, which are all present. The script for this challenge takes the value of `c` and raises it to the power of `d` modulo `n` which finally decodes to a message.

Result: `ZD{Well Done you have decrypted correctly}`

---

### Level 3

![Level 3 screenshot](screenshots/screen-3.png)

This level requires parsing a private RSA key file. Private keys are usually stored as a Base64 encoded ASN.1 sequence of values. ASN.1 stands for Abstract Syntax Notation One and is a widespread interface description language that stores data structures in a very accessible and cross-platform way.

The following command will print the values in the private key:

`openssl asn1parse -in mykey2 -i`

The output is rather large, so I stored it in a comment at the top of the solution script. The [RSA Specifications Version 2.1 (RFC 3447)](https://tools.ietf.org/html/rfc3447#appendix-A.1.2) explains how and in which order to interpret the values. Here is an excerpt:

```text
RSAPrivateKey ::= SEQUENCE {
  version           Version,
  modulus           INTEGER,  -- n
  publicExponent    INTEGER,  -- e
  privateExponent   INTEGER,  -- d
  prime1            INTEGER,  -- p
  prime2            INTEGER,  -- q
  exponent1         INTEGER,  -- d mod (p-1)
  exponent2         INTEGER,  -- d mod (q-1)
  coefficient       INTEGER,  -- (inverse of q) mod p
  otherPrimeInfos   OtherPrimeInfos OPTIONAL
}
```

The solution script uses the values obtained and prints them in the required format.

Result: `ZD{25804750360904248224329381618104859031736073222395248860499133051128513648896523325052435992237099000924849024564826844234697029915822571039994777064514824635243492963301478168480948385273501322600327794162141312212647635059765199895820389754402745012084674140342116327728380193544092902468871988407101113210818201750378837933282937750636399588218292079918162950294282004250547116764896324653457065316101365613347914317959505469586731762453963212022535424803572822031093301253062385003468990260150084465026582297271243286096414015105084255301102689693963566336024015793743350044649378818363190804537712326729609503119,65537,25564173244610971210351548452585197331194535758994673657884351015114666175874020376311922413781312689534869581593541780807512387877301314484073132668426835287971970400465565582293880630212968962130535153634911375813942663745522611172864711921423815900248860235223648392420965446176110834882493594752879241898541637225074107295433979711279703743206408857411263301020537809364614125840424406332180800207630227259634428188684178985515460114123914453650465520564263249152086786817100938246123146166512963816583276055667323176816331368813221646162976565638562106256552057858358804329568634212548081342870432443412497223185}`

---

### Level 4

![Level 4 screenshot](screenshots/screen-4.png)

Now we have to decrypt a message using a private key. Just like in Level 3, the first thing to do is to run:

`openssl asn1parse -in mykey3 -i`

Grabbing the needed values for decryption - `d` and `n` - along with our ciphertext, we can obtain the plaintext using the same procedure as in Level 2, which is what the solution script does.

Result: `ZD{OK time to move onto some harder stuff}`

---

### Level 5

![Level 5 screenshot](screenshots/screen-5.png)

Here we are given a file with some values, but `e` and `d` are missing. [The Wikipedia page for RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Using_the_Chinese_remainder_algorithm) explains how to retrieve a message in this scenario, with the help of the Chinese remainder algorithm.

The solution script follows the steps described in that section. Usually `m1` and `m2` are not the same, but in this case they were and so they both stored the message `m`.

This method of RSA decryption, although unorthodox, is used by many popular cryptographic libraries (such as OpenSSL) mainly for efficiency.

Result: `Those extra private key values are meant to make it easier?`

---

### Level 6

![Level 6 screenshot](screenshots/screen-6.png)

The values provided are `e`, `p`, `q` and `c`, and we must get `m`.

We know that for decryption we must have `d` and `n`. Luckily, the given file contains all the necessary information to construct those two values.

We can create `n` by multiplying its prime factors `p` and `q`. And we can make `d` by taking the modular inverse of `e`, and a common multiple of `p-1` and `q-1` which is most easily obtained by multiplying the two.

Once we have `d` and `n`, we can just repeat the steps from Level 2 to get the plaintext message. The script employs the use of the `gmpy2` module for help with finding the modular inverse.

Result: `You are doing very well, you must be starting to understand RSA by now!`

---

### Level 7

![Level 7 screenshot](screenshots/screen-7.png)

For this level we are only given the public key. Parsing it reveals two values - `n` and `e`. Normally this isn't enough to decrypt a ciphertext, but weakly generated keys can have flaws.

RSA relies on the strength of the modulus `n` in that, ideally, its prime factors `p` and `q` (or more, in rare cases) should be very large and chosen completely at random, with no possible way of predicting them. Without this being true, the whole system falls apart.

One way of testing the strength of a key is to check if its modulus has been factorised before. If it has, then it's trivial to recover the corresponding private key.

A great resource for this is [factordb](http://factordb.com), which successfully returned a result after I tested the modulus from this level. One of the factors was 3133337 which is incredibly small for a 2070 bit modulus.

Knowing `p` and `q`, we can now repeat the steps from Level 6 and decrypt `c`.

Result: `Only 4 more challenges to go!`

---

### Level 8

![Level 8 screenshot](screenshots/screen-8.png)

We are given the same setup as in the previous level - `n`, `e` and `c`. Trying to factorise `n` on factordb didn't work, but one other thing stands out. The public exponent is tiny.

We know that to encrypt a message we simply raise it to the power of `e` and then modulo `n`, but if the message was never large enough to begin with to require a modulo (a safe assumption, based on the sizes of previous `m` values), then the ciphertext itself is `m` to the power of `e`. So calculating `m` would simply involve getting the cube root of `c`. But `c` is so large, how would we do that?

Well, I cheated... sort of. I didn't use traditional ways of working with numbers, but instead I manipulated strings and used Python's versatility to help recover the `e`'th root of a number. The function in question - `get_m()` - was born in solve9.py and made its way to solve8.py in no time.

To briefly describe its functionality, here is what it does:

1. Finds the length of the `e`'th root of a given number `c`.
2. Traverses its length, one digit at a time, incrementing each digit until the whole number (in that state) to the power of `e` is greater than `c`.
3. Decrements the number that overflowed `c` and continues with the next digit until the end.
4. If at any point the number to the power of `e` equals `c`, the number is returned.

So it is esentially a brute force with major speed-ups due to how easily Python handles type conversions. Brilliant!

Once the script finds `m`, it is decoded to produce the solution.

Result: `We always need to watch the size of our message`

---

### Level 9

![Level 9 screenshot](screenshots/screen-9.png)

This level provides nine values - three sets of `e`, `n` and `c`. The challenge context implies that the same message was sent using each of these sets of values `n` and `e`.

A known attack on RSA exists for this scenario, known as Hastad's Broadcast Attack. It is detailed in a paper by Dan Boneh called Twenty Years of Attacks on the RSA Cryptosystem. The way he describes it, the attack is very specific and for simplicity the following requirements have been predisposed:

1. The number of ciphertexts `k` must be greater than or equal to `e`.
2. The greatest common divisor (GCD) of all combinations of `n` except with itself (e.g. gcd of `n1` and `n2`) must be equal to 1.
3. The message is less than each of the `n` values.

Dan Boneh then suggests using the Chinese Remainder Theorem (CRT) to find the common value `c` such that `c1 = c mod n1` and `c2 = c mod n2` and `c3 = c mod n3`. Then, knowing `c`, we can repeat the steps from Level 8 to get the `e`'th root of `c`, which in this case is the cube root.

The solution script implements an efficient CRT algorithm, and the `get_m()` function takes care of finding the cube root of the output from `crt()`.

Result: `Impressive: small_e_is_the_killer 38247601923468`

---

### Level 10

![Level 10 screenshot](screenshots/screen-10.png)

In Level 10, we are given some interesting values. We have `n1`, `e1`, `c1` and `n2`, `e2`, `c2`. What is interesting is that `n1` and `n2` are the same. [A write up from Codeblue CTF 2017](https://theromanxpl0it.github.io/ctf_codeblue2017/2017/11/10/common1.html) gives a nice explanation of an attack, known as the Common Modulus attack.

There is a theorem in mathematics called [Bézout's identity](https://en.wikipedia.org/wiki/Bézout's_identity) which states that, for any two integers `a` and `b` with a greatest common divisor of d, there exist integers `x` and `y` such that `ax + by = d`.

With that in mind, we can recover `m` if we have `c1` and `c2` and if the GCD of `e1` and `e2` is 1. Substituting `a` and `b` with `e1` and `e2`, we need to find `x` and `y` via the Extended Euclidean algorithm EGCD (also XGCD).

I used some code from a [Gist on Github](https://gist.github.com/siddhant3s/7970903) to implement the EGCD algorithm. As expected, it found that `d` is 1, but it also found `x` and `y`. If either of them are negative, their respective `a` or `b` value is modularly inverted with the common `n`, and the negative value is converted to its absolute (positive) value. From this, we can say that `e1*x + e2*y = 1` whenever it comes up.

Following some basic mathematical logic, we can compute `m` as follows (assuming `mod n` for all of the calculations):

```text
c = m pow e
c1 pow x = (m pow e1) pow x
c1 pow x = m pow (e1*x)
c1 pow x * c2 pow y = m pow (e1*x) * m pow (e2*y)
c1 pow x * c2 pow y = m pow (e1*x + e2*y)
c1 pow x * c2 pow y = m pow 1
...and finally...
m = (c1 pow x mod n) * (c2 pow y mod n) mod n
```

Based on the fact above, the solution script calculates `m` from the data we already know.

Result: `Only one more to go.. the force is strong with this one!`

---

### Level 11

![Level 11 screenshot](screenshots/screen-11.png)

For this final challenge we are given an unusual combination of RSA parameters - `c`, `n`, `e` and `dp`. Trying all previous attacks against `n` didn't work. There must be a reason that `dp` is given, and maybe it is enough to calculate `m`.

[I consulted the RFC](https://tools.ietf.org/html/rfc3447#section-2) again to understand what is happening, and to see what `dp` represents. The explanation given is that `dp * e = 1 (mod (p-1))`, which helps since `p` is in the equation as is the only unknown. Since `p-1` is modulo of the whole equation, there will be some brute forcing.

Because the above is true, we can rearrange the equation to say that `dp * e - 1 = 0 (mod (p-1))` and, since there is a zero remainder for `mod (p-1)`, it means that `dp * e - 1` divides evenly into `p-1` pieces. We can then say that `dp * e - 1` (let's call it `mp`) is a multiple of `p-1`. (PS: this part took me the longest to understand, despite its simplicity.)

What does that help us with? Simply that, if we divide `mp` by some number `k` and add 1, we will eventually get `p` after trying several `k` values, since `mp / k = p - 1` as we've already established. Testing for `p` is as simple as seeing if `n` modulo `mp / k + 1` equals zero.

My script solve11.py neatly implements this in one line using Python's generator expression syntax, and the rest is a piece of cake!

Result: `Go take a well earned break.. Happy holidays.`
