#Submitted
import sys

all_words = {}

def defining_words(command):
    if command[0] == "def":
        all_words[command[1]] = int(command[2])

def calculating_words(command):
    if command[0] != "calc":
        return "unknown"
    
    words_in_calc = []
    operators = []
    i = 1
    while i < len(command) and command[i] != '=':
        if i % 2 == 1:
            word = command[i]
            words_in_calc.append(word)
            if word not in all_words:
                return "unknown"
        else:
            op = command[i]
            operators.append(op)
        i += 1
    
    if not words_in_calc:
        return "unknown"
    
    numeric = []
    for word in words_in_calc:
        numeric.append(all_words[word])
        if operators:
            numeric.append(operators.pop(0))
    
    return evaluate(numeric)

def evaluate(numeric):
    if not numeric:
        return "unknown"
    
    if len(numeric) == 1:
        result = numeric[0]
    else:
        if len(numeric) % 2 == 0:
            return "unknown"
        
        result = numeric[0]
        for i in range(1, len(numeric), 2):
            op = numeric[i]
            if i + 1 >= len(numeric):
                return "unknown"
            num = numeric[i + 1]
            if op == '+':
                result += num
            elif op == '-':
                result -= num
            else:
                return "unknown"
    
    possible_keys = [k for k, v in all_words.items() if v == result]
    return possible_keys[0] if len(possible_keys) == 1 else "unknown"

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    command = line.split()
    if command[0] == "def":
        defining_words(command)
    elif command[0] == "calc":
        original_calc = ' '.join(command[1:])
        answer = calculating_words(command)
        print(f"{original_calc} {answer}")
    elif command[0] == "clear":
        all_words.clear()