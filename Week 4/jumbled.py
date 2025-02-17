#Submitted

def all_permutations():
    permutations = []
    encoded = []

    for i in range(256):
        permutations.append(format(i, '08b'))
        encoded.append(encode_byte(format(i, '08b')))

    return permutations, encoded

def encode_byte(x):
    x = int(x, 2)
    encoded = x ^ ((x << 1) & 0xFF)
    return encoded

def process_decode(bytes):
    permutations, encoded = all_permutations()
    for i in range(len(permutations)):     
        if str(encoded[i]) in curr_list:
            index = curr_list[str(encoded[i])]
            org_dex = int(permutations[i],2)
            for i in index:
                ans[i] = org_dex
    print(str(ans).replace('[','').replace(']','').replace(',','').strip())



curr_list = {}
number_of_bytes = int(input())
ans = [0] * number_of_bytes
bytes = input().strip().split()
for i in range(number_of_bytes):
    if bytes[i] in curr_list:
        curr_list[bytes[i]].append(i)
    else:
        curr_list[bytes[i]]=[i]
process_decode(bytes)



