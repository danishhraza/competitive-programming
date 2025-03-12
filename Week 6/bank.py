#Submitted
import heapq

num_people, time_left = input().strip().split()

num_people = int(num_people)
time_left = int(time_left)

sum = 0

max_heap = []

people_details = {}

for _ in range(num_people):
    cash, leave_in = input().strip().split()

    cash = int(cash)
    leave_in = int(leave_in)

    if leave_in in people_details:
        people_details[leave_in].append(cash)
    else:
        people_details[leave_in] = [cash]


for current_time in range(time_left -1, -1, -1):
    for leave_in in list(people_details.keys()):
        if leave_in >= current_time:
            for cash in people_details[leave_in]:
                heapq.heappush(max_heap, -cash)
            del people_details[leave_in]
    
    if max_heap:
        sum += -heapq.heappop(max_heap)
        

print(sum)