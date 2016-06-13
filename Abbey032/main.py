def getWinner(people, step):
    xs = [ i for i in range(1,people+1) ]

    counter = 0
    alive = []
    while (len(xs) > 1):
        for i in range(len(xs)):
            if (counter == step):
                counter = 0
            else:
                alive.append(xs[i])
                counter += 1
        xs = alive
        alive = []

    return xs[0]

def main():
    print("initial data:")
    people, step = [ int(x) for x in input().split() ]
    w = getWinner(people, step-1)

    print("\nanswer:")
    print(str(w))

main()
