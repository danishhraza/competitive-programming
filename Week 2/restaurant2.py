def move_plates(stack_A, stack_B):
    plates_moved = len(stack_B)
    for _ in range(len(stack_B)):
        stack_A.append(stack_B.pop())
    print("MOVE 2->1", plates_moved)
    return (stack_A, stack_B)

def wash_plates(stack_A, num_plates):
    plates_washed = 0
    while len(stack_A) != 0 or plates_washed < num_plates:
        stack_A.pop()
        plates_washed += 1
    print("TAKE 1", plates_washed)
    return (plates_washed, stack_A)

def take_plates(stack_A, stack_B, num_plates):
    plates_washed = 0
    if len(stack_A) != 0:
        plates_washed, stack_A = wash_plates(stack_A, num_plates)
    if plates_washed < num_plates:
        plates_left = num_plates - plates_washed
        stack_A, stack_B = move_plates(stack_A, stack_B)
        plates_washed, stack_A = wash_plates(stack_A, plates_left)
        return stack_A, stack_B

def process_instructions(instructions):
    stack_A = []
    stack_B = []
    for i in range(len(instructions)):
                    
        if instructions[i][0] == "DROP":
            for j in range(int(instructions[i][1])):
                stack_B.append("plate")
            
            print("DROP 2", instructions[i][1])
    
        if instructions[i][0] == 'TAKE':
            if len(stack_A) == 0:
                (stack_A, stack_B) = move_plates(stack_A, stack_B) # ok
            stack_A, stack_B = take_plates(stack_A, stack_B, int(instructions[i][1]))

while True:
    instructions = []
    num_cases = int(input())
    if num_cases == 0 or num_cases > 50:
        break
    else:
        for _ in range(num_cases):
            instruction = input().split()
            instructions.append(instruction)

        process_instructions(instructions)
        print()