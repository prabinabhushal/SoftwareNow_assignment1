# TASK 1: Character Census

text = input("Enter anything: ")

total_chars   = 0
letter_count  = 0
digit_count   = 0
space_count   = 0
other_count   = 0

for char in text:
    total_chars += 1          

    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char.isspace():
        space_count += 1
    else:
        other_count += 1

# Self check - The below code iss the four categories that must add up to the total
check_sum = letter_count + digit_count + space_count + other_count

print()
print("=" * 49)
print("CHARACTER CENSUS REPORT".center(49))
print("=" * 49)
print(f"Total characters                       : {total_chars}")
print(f"Total Letters (a-z, A-Z)               : {letter_count}")
print(f"Total Digits (0-9)                     : {digit_count}")
print(f"Total Whitespace                       : {space_count}")
print(f"Total of other characters              : {other_count}")
print("-" * 49)
print(f"Self check (sum of 4 categories)       : {check_sum}")
if check_sum == total_chars:
    print("Self check PASSED — Categories match the total!.")
else:
    print("Self check FAILED — something was miscalculated!")
print("=" * 49)
