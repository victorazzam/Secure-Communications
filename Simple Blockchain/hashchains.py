import hashlib

chain, target = "ecsc", "c89aa2ffb9edcc6604005196b5f0e0e4"
while hashlib.md5(chain.encode()).hexdigest() != target:
    chain = hashlib.md5(chain.encode()).hexdigest()

print(chain)
