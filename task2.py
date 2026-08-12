# TASK 2: Case and Vowel Breakdown



text = input("Enter a text : ")



# Counters

upper_count      = 0

lower_count      = 0

vowel_count      = 0

consonant_count  = 0





vowel_statistics = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

vowels = "aeiou"



for char in text:

    if char.isalpha():



        # Case check 

        if char.isupper():

            upper_count += 1

        elif char.islower():

            lower_count += 1



        # Vowel/consonant check 

        lower_char = char.lower()          

        if lower_char in vowels:

            vowel_count += 1

            vowel_statistics[lower_char] += 1

        else:

            consonant_count += 1



print()

print("=" * 27)

print("CASE & VOWEL BREAKDOWN".center(27))

print("=" * 27)

print(f"Uppercase letters    : {upper_count}")

print(f"Lowercase letters    : {lower_count}")

print(f"Vowels               : {vowel_count}")

print(f"Consonants           : {consonant_count}")

print("-" * 27)

print("Individual vowel frequency:")

for v in vowels:

    print(f"  {v} : {vowel_statistics[v]}")

print("=" * 27)