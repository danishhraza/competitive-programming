#Submitted
while True:
    n = int(input().strip())
    if n == 0:
        break

    files = [input() for _ in range(n)]

    xor_hashes = []
    for f in files:
        result = 0
        for ch in f:
            result ^= ord(ch)
        xor_hashes.append(result)

    hash_map = {}         
    collision_count = 0
    unique_files = 0

    for i, h in enumerate(xor_hashes):
        if h not in hash_map:
            hash_map[h] = [i]
            unique_files += 1
        else:
            collisions_for_this_file = 0
            matched = False
            for prev_idx in hash_map[h]:
                if files[i] != files[prev_idx]:
                    collisions_for_this_file += 1
                else:
                    matched = True
            collision_count += collisions_for_this_file

            if not matched:
                unique_files += 1

            hash_map[h].append(i)

    print(unique_files, collision_count)
