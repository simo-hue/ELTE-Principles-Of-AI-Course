def create_adders():
    return [lambda x, n=n: x + n for n in [10, 20, 30]]

adders = create_adders()

print(adders[0](5))
print(adders[1](5))
print(adders[2](5))