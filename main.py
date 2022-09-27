import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "{}[]()/_-;"
All = lower + upper + numbers + symbols

passlen = int(input("How many characters do you want in your password: "))
password = "".join(random.sample(All, passlen))
print(password)
