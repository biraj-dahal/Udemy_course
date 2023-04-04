import random
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0192837465"
symbols = "!#$%&()*+_"
print("Welcome ot the Strong password Generator. ")
n_of_characters = int(input("Enter the number of characters you want in your password: "))
n_of_digits = int(input("Enter the number of digits you want in your password: "))
n_of_symbols = int(input("Enter the number of symbols you want in your password: "))

pass_list = []
for _ in range(n_of_characters):
    pass_list.append(random.choice(characters))
for _ in range(n_of_digits):
    pass_list.append(random.choice(digits))
for _ in range(n_of_symbols):
    pass_list.append(random.choice(symbols))
random.shuffle(pass_list)
print("".join(pass_list))

