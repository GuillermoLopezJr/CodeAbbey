def main():
    print("input data:")
    WIDTH, HEIGHT, LENGTH = map(int, input().split())
    x = y = 0
    velX = velY = 1

    for _ in range(101):
        print(x,y, end=' ')
        x += velX
        y += velY

        if (x <= 0) or ((x+LENGTH) >= WIDTH):
            velX *= -1
        if (y <= 0) or (y >= (HEIGHT-1)):
            velY *= -1

main()
