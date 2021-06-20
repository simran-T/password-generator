import random 
import string

length = int(input("Enter the length of the password: "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

pass_list = random.sample(all, length)

password = "".join(pass_list)

print(password)