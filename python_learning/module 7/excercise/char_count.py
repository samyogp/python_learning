# this is the count character frequency example in python.

text = input("Enter a string: ")
char_count = {}
for ch in text:
    char_count[ch] = char_count.get(ch, 0) + 1
print(char_count)
