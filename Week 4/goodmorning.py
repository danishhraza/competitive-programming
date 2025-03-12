#Submitted
num = {
    '1': {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'},
    '2': {'2', '3', '5', '6', '8', '9', '0'},
    '3': {'3', '6', '9'},
    '4': {'4', '5', '6', '7', '8', '9', '0'},
    '5': {'5', '6', '8', '9', '0'},
    '6': {'6', '9'},
    '7': {'7', '8', '9', '0'},
    '8': {'8', '9', '0'},
    '9': {'9'},
    '0': {'0'},
}

def can_input(n):
    n = str(n)
    for i in range(len(n) - 1):
        if n[i + 1] not in num[n[i]]:
            return False
    return True

def findClosestValidK(k):
    k = int(k)
    i = 0
    while True:
        if can_input(k + i):
            return k + i
        if k - i > 0 and can_input(k - i):
            return k - i
        i += 1

size = int(input())
for _ in range(size):
    k = input()
    print(findClosestValidK(k))
