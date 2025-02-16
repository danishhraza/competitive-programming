#Submitted

#Data Structure used: Union Find

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, size, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)

    if rootX != rootY:
        if size[rootX] < size[rootY]:
            rootX, rootY = rootY, rootX
        parent[rootY] = rootX
        size[rootX] += size[rootY]

def add(parent, size, x):
    if x not in parent:
        parent[x] = x
        size[x] = 1

def form_network(friends, parent, size):
    friend1, friend2 = friends

    add(parent, size, friend1)
    add(parent, size, friend2)
    union(parent, size, friend1, friend2)

    root = find(parent, friend1)
    print(size[root])

num_cases = int(input())

for _ in range(num_cases):
    number_friends_formed = int(input())
    parent = {}
    size = {}
    for _ in range(number_friends_formed):
        friends = input().strip().split()
        form_network(friends, parent, size)