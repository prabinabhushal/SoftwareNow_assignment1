# TASK 4: Line and Sentence Analysis

text = input("Enter anything you need: ")

line_count = 0
sentence_count = 0
current_line_length = 0
longest_line_length = 0

if len(text) > 0:
    line_count = 1

for char in text:
    if char == '\n':
        if current_line_length > longest_line_length:
            longest_line_length = current_line_length
        current_line_length = 0   
        line_count += 1       
    else:
        current_line_length += 1  

        if char == '.' or char == '!' or char == '?':
            sentence_count += 1

if current_line_length > longest_line_length:
    longest_line_length = current_line_length

print()
print("~" * 36)
print("LINE & SENTENCE ANALYSIS".center(36))
print("~" * 36)
print(f"> Total Number of lines        : {line_count}")
print(f"> Total Number of sentences    : {sentence_count}")
print(f"> Longest line (chars)         : {longest_line_length}")
print("~" * 36)