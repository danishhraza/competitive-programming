def sumOfDigits(num):
    sum = num % 10
    while num > 0:
        num = num // 10
        digit = num % 10
        sum += digit
    return sum

def closestNum(num):
    sumOfNum = sumOfDigits(num)
    required = sumOfNum - 1
    for i in range(num-1, 0, -1):
        if sumOfDigits(i) == required:
            return i
    return 0

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        print(closestNum(N))
main()