import sys

all_words = {}

def defining_words(command):
    if command[0] == "def":
        all_words[command[1]] = int(command[2])

def calculating_words(command):
    words_in_calc = []
    numeric = []    
    if command[0] == "calc":
        for i in range(1, len(command), 2):
            words_in_calc.append(command[i])
            if command[i] not in all_words:
                return "unknown"
        j = 0
        for i in range(2, len(command), 2):
            numeric.append(all_words[words_in_calc[j]])
            j +=1
            if command[i] != "=":
                numeric.append(command[i])
        
        result = evaluate(numeric)
        return result

def evaluate(numeric):
    if numeric[1] == "+":
        result = int(numeric[0]) + int(numeric[2])
    if numeric[1] == "-":
        result = int(numeric[0]) - int(numeric[2])
    if len(numeric)>3:
        for i in range(3, len(numeric), 2):
            if numeric[i] == "+":
                result = result + int(numeric[i+1])
            if numeric[i] == "-":
                result = result - int(numeric[i+1])
    key = [key for key, val in all_words.items() if val == result]
    if key:
        answer = key[0]
        return answer
    else:
        return "unknown"

# Read all input lines at once
for line in sys.stdin:
    command = line.strip().split()
    
    if command[0] == "def":
        defining_words(command)
    elif command[0] == "calc":
        answer = calculating_words(command)
        print(" ".join(command[1:]), answer)
    elif command[0] == 'clear':
        all_words = {}