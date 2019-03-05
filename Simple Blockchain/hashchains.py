import hashlib

# Seed is MD5 of inverted case of string

hashchain = "ecsc"
while hashchain != "c89aa2ffb9edcc6604005196b5f0e0e4":
	hash_for_the_win = hashchain
	hashchain = hashlib.md5(hashchain.encode()).hexdigest()
print(hash_for_the_win)
