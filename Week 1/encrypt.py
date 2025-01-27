import math

num_messages = int(input())

messages = [input() for _ in range(num_messages)]

encrypted_messages = []

for message in messages:
    L = len(message)
    Y = math.ceil(math.sqrt(L))
    table = []
    M = Y*Y
    asterisks_count = M - L
    asterisks = '*' * asterisks_count
    padded_message = f"{message}{asterisks}"
    output = ""

    for i in range(Y):
        row = list(padded_message[i*Y:(i+1) * Y])
        table.append(row)

    res = [[0]* Y for _ in range(Y)]

    for i in range(Y):
        for j in range(Y):
            res[j][Y-i-1] = table[i][j]

    for row in res:
        for element in row:
            if element != '*': 
                output+=element
    print(''.join(output))


