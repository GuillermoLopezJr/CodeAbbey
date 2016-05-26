print("input data:")
words = input().split()

for i in range(len(words)):
    word = list(words[i])
    word.reverse()
    words[i] = (''.join(word))

words.reverse()
print("\nanswer:")
print(' '.join(words))
