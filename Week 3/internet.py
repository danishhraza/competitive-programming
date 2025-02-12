

def prefixSum(array):
    if not array:
        return []
    
    prefix_sum = [0] * len(array)
    difference = [0] * len(prefix_sum)

    prefix_sum[0] = array[0]
    difference[0] = 47 - prefix_sum[0]

    count = 0

    for i in range(1, len(array)):
            prefix_sum[i] = array[i] + prefix_sum[i-1]
            difference[i] = 47 - prefix_sum[i]

            if difference[i] == 0:
                count+=1

            if -difference[i] in prefix_sum:
                count+=1

    print(prefix_sum)
    print(difference)
    print(count)
    return prefix_sum, difference, count


# def find_47_in_prefix_sum(prefix_sum, difference):
#     count = 0
#     count += difference.count(0)

#     for i in range(len(prefix_sum)):
#         if -prefix_sum[i] in difference:
#             count+=1

#     print(count)
#     return count


num_cases = int(input())

for _ in range(num_cases):
    _input = input()
    if _input == '\n':
         continue
    seq = []
    seq_length = int(input())
    seq = input().strip().split()
    if len(seq)>seq_length:
        break
    seq = list(map(int, seq))
    prefix_sum, difference, count = prefixSum(seq)
    
    # find_47_in_prefix_sum(prefix_sum, difference)

