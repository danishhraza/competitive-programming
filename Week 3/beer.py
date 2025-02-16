
def manhattan_distance(cord1, cord2):
    return abs(int(cord1[0]) - int(cord2[0])) + abs(int(cord1[1]) - int(cord2[1]))


def process_map(map):

    distance = [0] * len(map)
    
    current_cord = map[0]

    for i in range(map[current_cord:]):
        if i == 0:
            distance[0] == 0
        else:
            if map[i] != current_cord:
                cord1 = current_cord
                cord2 = map[i]
                distance[i] = manhattan_distance(cord1, cord2)

                if distance[i] <= 1000:
                    current_cord = map[i]
    
            
    print(distance)
    return "happy"


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