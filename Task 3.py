# TASK 3: Word Statistics

text = input("Enter a text: ")

current_word    = ""    
word_count      = 0
total_length    = 0
longest_word    = ""
longest_length  = 0

for char in text:
    if char.isalpha() or (char == "'" and current_word != ""):
        current_word += char
    else:
        if current_word != "":
            word_count += 1
            word_length = len(current_word)
            total_length += word_length

            if word_length > longest_length:
                longest_length = word_length
                longest_word = current_word

            current_word = ""  

if current_word != "":
    word_count += 1
    word_length = len(current_word)
    total_length += word_length

    if word_length > longest_length:
        longest_length = word_length
        longest_word = current_word

    current_word = ""

# Calculating average
if word_count > 0:
    average_length = total_length / word_count
else:
    average_length = 0

print()
print("=" * 35)
print("WORD STATISTICS".center(35))
print("=" * 35)
print(f"Total words           : {word_count}")
print(f"Longest word          : '{longest_word}'")
print(f"Longest word length   : {longest_length}")
print(f"Average word length   : {round(average_length, 1)}")
print("=" * 35)