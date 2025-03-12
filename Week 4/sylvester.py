def hadamard_element(i, j):
    return 1 if bin(i & j).count('1') % 2 == 0 else -1

def printPartialHadamard(n, x, y, w, h):
    for i in range(h):
        line = ""
        for j in range(w):
            element = hadamard_element(i + y, j + x)
            line += str(element) + ' '
        print(line)

# Example usage
size = int(input())
for _ in range(size):
    n, x, y, w, h = map(int, input().split())
    printPartialHadamard(n, x, y, w, h)
