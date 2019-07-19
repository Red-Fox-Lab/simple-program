#You enter the number
#The program shows you the collection of simple numbers you can divide your number with

while True:
    v = int(input("Write number: "))
    t = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    natural = range(1, 1000000)
    for n in t:
        for z in natural:
            if v/n == z:
                g = v/n
                print(f"{n} ({round(g)} times)")