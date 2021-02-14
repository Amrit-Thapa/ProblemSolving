num = int(input("enter any number.. ! \n"))


def uper_half(num):
    row = col = count = lower = num
    # upper half
    for i in range(0, num):
        row = num
        for j in range(i + 1):
            print(row, end=" ")
            row = row - 1

        for k in range(i, num - 1):
            print(col, end=" ")

        for l in range(i, num - 1):
            print(col, end=" ")
        col = col - 1
        count = count - i
        for m in range(i):
            print(count + 1, end=" ")
            count = count + 1

        print()


def lower_half(num):
    row = col = count = lower = num
    for i in range(0, num - 1):
        row = num

        for j in range(i, num - 1):
            print(row, end=" ")
            row = row - 1

        for k in range(i + 1):
            print(i + 2, end=" ")

        for l in range(i + 1):
            print(i + 2, end=" ")
        count = num - (col - 3)
        for m in range(col - 2):
            print(count, end=" ")
            count += 1
        col = col - 1
        print()


uper_half(num)
lower_half(num)