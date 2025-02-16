#Submitted

#Data structure used: BFS


from collections import deque

def manhattan_distance(cord1, cord2):
    return abs(int(cord1[0]) - int(cord2[0])) + abs(int(cord1[1]) - int(cord2[1]))

def process_map(map):
    n = len(map)
    visited = [False] * n
    queue = deque([0])  # Jo's home
    visited[0] = True

    while queue:
        current = queue.popleft()
        current_cord = map[current]

        for i in range(n):
            if not visited[i]:
                cord = map[i]
                if manhattan_distance(current_cord, cord) <= 1000:
                    queue.append(i)
                    visited[i] = True
                    if i == n - 1:  
                        return "happy"
    
    return "sad"

test_cases = int(input())

for _ in range(test_cases):
    number_of_stops = int(input())
    map = []
    house_address = input().strip().split()
    map.append(house_address)

    for _ in range(number_of_stops):
        shop_address = input().strip().split()
        map.append(shop_address)

    destination_address = input().strip().split()
    map.append(destination_address)

    emotion = process_map(map)
    print(emotion)