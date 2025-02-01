num = int(input("Enter the number: "))

if num < 1000:
    print("\nIt's not a 4 or more digit number!")
else:
    t = num
    numLen = 0

    while t > 0:
        numLen += 1
        t = int(t / 10)

    if numLen >= 4:
        numLen = int(numLen / 2)

    chk = 0
    midOne, midTwo = None, None

    while num > 0:
        rem = num % 10
        if chk == numLen:
            midOne = rem
        elif chk == (numLen - 1):
            midTwo = rem
        num = int(num / 10)
        chk += 1

    if midOne is not None and midTwo is not None:
        prod = midOne * midTwo
        print(f"\nProduct of Mid digits ({midOne} * {midTwo}) = {prod}")
