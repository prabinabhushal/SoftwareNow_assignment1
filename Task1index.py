# Task 1: Character Census

text = input('Enter a block of text: ')

total_characters = 0
letters = 0
digits=0
whitespace=0
other_characters=0

# calculate total characters
for char in text:
    total_characters +=1

# calculate letters
for char in text:
    if char.isalpha():
        letters += 1

# calculate digits
for char in text:
    if char.isdigit():
        digits += 1

# calculate whitespace
for char in text:
    if char.isspace():
        whitespace +=1

# calculate other characters
for char in text:
    if not char.isalpha() and not char.isdigit() and not char.isspace():
        other_characters +=1

print('\nResult:')
print('1. Total characters: ', total_characters)
print('2. Letters: ', letters)
print('3. Digits: ', digits)
print('4. Whitespace: ', whitespace)
print('5. Other characters: ', other_characters)




