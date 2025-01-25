def flexible(roomWidth, partitionLocations):
    all_partitions = [0] + partitionLocations + [roomWidth]
    all_distinct_partitions = []

    for i in range(len(all_partitions)):
        for j in range(i+1, len(all_partitions)):
            all_distinct_partitions.append(all_partitions[j] - all_partitions[i])

    all_distinct_partitions = sorted(set(all_distinct_partitions)) 

    print(all_distinct_partitions)

flexible(6, [2,5])