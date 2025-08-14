base = float(input("Enter the base number: "))

n = int(input("Enter the maximum exponent: "))

print(f"Powers of {base} from 1 to {n}:")

for i in range(1, n+1):

   print(f"{base}^{i} = {base ** i}")