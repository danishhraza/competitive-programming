#Submitted
from itertools import combinations

def euclidean_distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def walls(craneRange, craneLocations, wallCentres):
    crane_coverage = {}  
    wall_coverage = {i: [] for i in range(len(wallCentres))}

    for i, crane in enumerate(craneLocations):
        covered_walls = set()
        for j, wall in enumerate(wallCentres):
            if euclidean_distance(crane, wall) <= craneRange:
                covered_walls.add(j)
                wall_coverage[j].append(i)
        crane_coverage[i] = covered_walls

    required_walls = set(range(len(wallCentres))) 

    for crane, covered_walls in crane_coverage.items():
        if covered_walls == required_walls:
            return 1 

    for r in range(2, 5): 
        for crane_set in combinations(crane_coverage.keys(), r):
            combined_coverage = set()
            for crane in crane_set:
                combined_coverage.update(crane_coverage[crane])
            if combined_coverage == required_walls:
                return r  
    return "Impossible"  

l,w,n,r =  map(int, input().strip().split(' '))

wallCentres = [
        (-l / 2, 0), (l / 2, 0),  
        (0, -w / 2), (0, w / 2)   
    ]

craneLocations = []
for _ in range(n):
    x, y = map(int, input().split())
    craneLocations.append((x, y))

print(walls(r, craneLocations, wallCentres))
