
while True:
    num_cases = int(input())
    if num_cases == 0 or num_cases > 50:
        break
    if num_cases <= 50:
        instructions = [input() for _ in range(num_cases)]
        print(instructions)