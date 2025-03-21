trick = list(input())

ball_index = 'A'


for i in range(len(trick)):

    if trick[i] == 'C':
        if ball_index == 'A':
            ball_index = 'C'
    
        elif ball_index == 'B':
            ball_index = 'B'

        elif ball_index == 'C':
            ball_index = 'A'

    elif trick[i] == 'A':
        if ball_index == 'A':
            ball_index = 'B'
    
        elif ball_index == 'B':
            ball_index = 'A'

        elif ball_index == 'C':
            ball_index = 'C'
    
    elif trick[i] == 'B':
        if ball_index == 'A':
            ball_index = 'A'
    
        elif ball_index == 'B':
            ball_index = 'C'

        elif ball_index == 'C':
            ball_index = 'B'

    

if ball_index == 'A':
    print(1)
elif ball_index == 'B':
    print(2)
elif ball_index == 'C':
    print(3)

