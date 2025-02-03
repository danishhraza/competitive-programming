
while True:
    num_cases = int(input())
    if num_cases == 0 or num_cases > 50:
        break
    if num_cases <= 50:
        instructions = [input().split() for _ in range(num_cases)]
        stack_A = []
        stack_B = []

        for i in range(len(instructions)):
            if instructions[i][0] == "DROP":
                for j in range(int(instructions[i][1])):
                    stack_B.append("plate")
                
                print("DROP 2", instructions[i][1])
                
            
            if instructions[i][0] == "TAKE":
                if  len(stack_A)==0 and len(stack_B)==0:
                    break
                    
                else:
                    if len(stack_A) == 0:
                        plates_moved = len(stack_B)
                        for j in range(len(stack_B)):
                            stack_A.append(stack_B.pop())

                        print("MOVE 2->1 ", plates_moved)

                    plates_washed = 0
                    while len(stack_A) != 0:
                        for j in range(int(instructions[i][1])):
                            plates_washed+=1
                            stack_A.pop()
                    if plates_washed<int(instructions[i][1]):
                        plates_left = int(instructions[i][1]) - plates_washed
                        for i in range(plates_left):
                            stack_A.append(stack_B.pop())
                    
                    print("TAKE 1", instructions[i][1])
        print()
