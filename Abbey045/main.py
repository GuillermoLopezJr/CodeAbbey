ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
suits = ['C', 'D', 'H', 'S']

def origDeck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(suit+rank)

    return deck

def swap(index1, index2, deck):
    index1 = index1 % 52
    temp = deck[index2]
    deck[index2] = deck[index1]
    deck[index1] = temp

def main():
    print("input data:")
    deck = origDeck()
    shuffles = list(map(int, input().split()))

    index2 = 0
    for index1 in shuffles:
        swap(index1,index2,deck)
        index2 += 1

    print("\nanswer: ")
    print(' '.join(deck))

main()
