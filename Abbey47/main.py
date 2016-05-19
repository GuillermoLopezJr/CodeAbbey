print("input data: ")
lines, shift = map (int, input().split())

sentences = []
for i in range(lines):
    sentence = input().split();
    sentences.append(sentence);

print("answer: ")
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for sentence in sentences:
    encryptedSentence = ""
    for word in sentence:
        encryptedWord = ""
        for ch in word:
            if(ch == '.'):
                continue
            encryptedIndex = (alpha.index(ch) - shift) % 26
            encryptedChar = alpha[encryptedIndex]
            encryptedWord += encryptedChar
        encryptedSentence += encryptedWord + " "
    #remove the space before the period
    encryptedSentence = encryptedSentence[:-1]   
    encryptedSentence += '.'
    print(encryptedSentence)
