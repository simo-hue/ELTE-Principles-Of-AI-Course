# Generating a list of multiplier lambdas
multipliers = [lambda x,i=i: x * i for i in range(4)]

# Executing each lambda with the argument 2
result = [m(2) for m in multipliers]

print(type(multipliers))
print(result)

#
#
#
#
#

# Generating a list of multiplier lambdas
multipliers = [lambda x: x * i for i in range(4)]

# Executing each lambda with the argument 2
result = [m(2) for m in multipliers]

print(type(multipliers))
print(result)