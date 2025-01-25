import random
import math

def encryption():
    message = "this is a message"
    L = len(message)
    Y = math.ceil(math.sqrt(L))
    print("Y is " + str(Y))
    table = []
    M = Y*Y
    print("Length is " + str(L) + ", Square is " + str(M))
    asterisks_count = M - L
    print("Asterisks to add " + str(asterisks_count))
    asterisks = '*' * asterisks_count
    padded_message = f"{message}{asterisks}"
    output = ""
    print(padded_message)


    for i in range(Y):
        row = list(padded_message[i*Y:(i+1) * Y])
        table.append(row)
    
    res = [[0]* Y for _ in range(Y)]

    for i in range(Y):
        for j in range(Y):
            res[j][Y-i-1] = table[i][j]


    for row in table:
        print(' '.join(map(str, row)))

    
    print("\n")
    

    for row in res:
        print(' '.join(map(str, row)))

    for row in res:
      for element in row:
         if element != '*': 
            output+=element
    print("Encrypted message is '" + ''.join(output) + "'")  
    

encryption()