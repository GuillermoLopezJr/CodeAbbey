suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

def getCard(cardVal):
    suitVal = cardVal // 13
    rankVal = cardVal % 13

    rank = ranks[rankVal]
    suit = suits[suitVal]
    
    return (rank + "-of-" + suit)

def main():
    print("input data:")
    TEST_CASES = int(input())
    cards = list(map(int, input().split()))

    ans = []
    for cardVal in cards:
        card = getCard(cardVal)
        ans.append(card)

    print("\nanswer:")
    print(' '.join(ans))

main()
