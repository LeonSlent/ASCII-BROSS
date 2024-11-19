elemento = " "

for y in range (30):
    for x in range (60):
        if x == 0 or x == 59 or y == 0 or y == 29:
            print ("x", end=" ")
        else:
            print (elemento, end=" ")
    print ()