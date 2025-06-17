import random

alphabets = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
numbers = [    
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]
symbols = [
    '!', '@', '#', '%', '$', '^', '&', '*', '(', ')', '_', '+', '=', '-', '{', '}',
    '|', '[', ']', ':', '"', ';', '>', '<', '?', ',', '.'
]

print("Welcome to the PyPassword Generator!")
alphabets_input = int(input("How many letters would like in your password?"))
numbers_input = int(input("How many numbers would you like?"))
symbols_input = int(input("How many symbols would you like?"))

alphabets_list = list(alphabets)   
numbers_list = list(numbers)            
symbols_list = list(symbols) 

random_alphabets = random.choices(alphabets_list, k=alphabets_input)
random_numbers = random.choices(numbers_list, k=numbers_input)
random_symbols = random.choices(symbols_list, k=symbols_input)

input_passwords = random_alphabets + random_numbers + random_symbols
passwords_list = list(input_passwords)

counting = 0

for x in passwords_list:
    counting += 1

passwords_generator = random.sample(passwords_list, k=counting)

passwords = ''.join(passwords_generator)
print(f"Your pasword is: {passwords}")
