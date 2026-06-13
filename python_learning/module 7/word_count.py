# word count example in python 

sentence = "apple banana apple orange banana apple"
words = sentence.split()
count = {}
for word in words:
    count[word] = count.get(word, 0) + 1
    print(count)
    