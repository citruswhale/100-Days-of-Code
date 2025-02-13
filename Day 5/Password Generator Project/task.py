import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

ans = ""

# for i in range(0, nr_letters):
#     ans += random.choice(letters)
# for i in range(0, nr_symbols):
#     ans += random.choice(symbols)
# for i in range(0, nr_numbers):
#     ans += random.choice(numbers)

options = []

for i in range(0, nr_letters):
    options.append(random.choice(letters))
for i in range(0, nr_symbols):
    options.append(random.choice(symbols))
for i in range(0, nr_numbers):
    options.append(random.choice(numbers))

random.shuffle(options)

for i in range(0, nr_letters+nr_numbers+nr_symbols):
    ans += options[i];
    # el = random.choice(options)
    # options.remove(el)
    # ans += el

print(ans)