def anagramCount(word, dictionary):
    count = -1 #because original word in dict
    for w in dictionary:
        if (len(w) == len(word)) and (sorted(w) == sorted(word)):
            count += 1

    return count

def fillList():
    f = open("words.txt", 'r')

    words = []
    for word in f:
        words.append(word.rstrip())

    return words

def main():
    print("input data:")
    TEST_CASES = int(input())
    dictionary = fillList()

    ans = []
    for _ in range(TEST_CASES):
        word = input()
        count = anagramCount(word, dictionary)
        ans.append(count)

    print("\nanswer:")
    print(' '.join(map(str, ans)))

main()
