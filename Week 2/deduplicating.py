
while True:
    file = []
    number_of_files = int(input())
    if number_of_files == 0:
        break
    for i in range(number_of_files):
        line = input()
        file.append(line)
    
    Results = []
    collision_count = 0
    for f in file:
        line_ascii = [ord(char)for char in f]
        result = line_ascii[0] ^ 0
        for i in range(1, len(line_ascii)):
            result = result ^ line_ascii[i]
        Results.append(result)
    
    print("Results array " + str(Results))
    
    hash_to_files = {}

    for idx, res in enumerate(Results):
        if res not in hash_to_files:
            hash_to_files[res] = set()
        hash_to_files[res].add(file[idx])
    
    collision_count = 0
    unique_files = 0

    for files_set in hash_to_files.values():
        if len(files_set) > 1:
            collision_count += sum(1 for _ in range(len(files_set))) - 1
    

    print("Unique files " + str(unique_files))
    print("Number of collisions " + str(collision_count))
    




