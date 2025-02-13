#SUBMITTED
def process_instructions(instructions):
    stack_A = 0
    stack_B = 0
    for i in range(len(instructions)):
        
        if instructions[i][0] == "DROP":
            amount_to_drop = int(instructions[i][1])
            stack_B += amount_to_drop
            print("DROP 2", amount_to_drop)

        
        if instructions[i][0] == "TAKE":
            amount_to_take = int(instructions[i][1])
            if stack_A == 0:
                stack_A = stack_B
                print("MOVE 2->1", stack_B)
                stack_B = 0
                stack_A -= amount_to_take
                print("TAKE 1", amount_to_take)
                
            
            elif stack_A<amount_to_take:
                amount_taken = stack_A
                print("TAKE 1", amount_taken)
                amount_to_take -= amount_taken
                amount_taken = 0
                stack_A = 0

                stack_A=stack_B
                print("MOVE 2->1", stack_B)
                stack_B = 0


                stack_A -= amount_to_take
                print("TAKE 1", amount_to_take)

            elif stack_A >= amount_to_take:
                stack_A -= amount_to_take
                print("TAKE 1", amount_to_take)



while True:
    instructions = []
    num_cases = int(input())
    if num_cases == 0:
        break
    
    for _ in range(num_cases):
            instruction = input().split()
            instructions.append(instruction)

    process_instructions(instructions)
    print()