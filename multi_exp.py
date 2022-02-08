# Multiplication/Exponentiation

my_name = input("Please enter your full name: ")

number = int(input("\nWhat number would you like to work with: "))
print(f"\nMultiplication Table for {number}. ")

for x in range(1, number + 1):
    res = x*number
    print(f"\t{x}*{number}={res}")

print(f"\nExponentiation Table for {number}. ")

for x in range(1, number + 1):
    res=x**number
    print(f"\t{x}^{number}={res}")    