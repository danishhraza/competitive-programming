
subs = {
    "at":"@",
    "and":"&",
    "one":"1",
    "won":"1",
    "to":"2",
    "too":"2",
    "two":"2",
    "four":"4",
    "for":"4",
    "bee":"b",
    "bea":"b",
    "be":"b",
    "sea":"c",
    "see":"c",
    "eye":"i",
    "oh":"o",
    "owe":"o",
    "are":"r",
    "you":"u",
    "why":"y"
}

def uppercase(word):
    return word.upper()


def encode(line):
    global subs
    lineArr = line.split(' ')
    outputArr = []
    # if word replaced, skip word length, otherwise increment by 1
    # Max word that can be replaced is of length 4, otherwise 3 or 2
    for i in range(0, len(lineArr)):
        j = 0
        word = lineArr[i]
        outputWord = ''
        while j < len(word):
            if j+4 <= len(word):
                check = word[j:j+4].lower()
                if check in subs:
                    replacement = subs[check]
                    if word[j].isupper():
                        replacement = uppercase(subs[check])
                    outputWord = outputWord + replacement
                    j += 4
                    continue

            if j+3 <= len(word):
                check = word[j:j+3].lower()
                if check in subs:
                    replacement = subs[check]
                    if word[j].isupper():
                        replacement = uppercase(subs[check])
                    outputWord = outputWord + replacement
                    j += 3
                    continue
            
            if j+2 <= len(word):
                check = word[j:j+2].lower()
                if check in subs:
                    replacement = subs[check]
                    if word[j].isupper():
                        replacement = uppercase(subs[check])
                    outputWord = outputWord + replacement
                    j+=2
                    continue
            outputWord = outputWord + word[j]
            j += 1
        outputArr.append(outputWord)

    response = ' '.join(outputArr)
    return response

    

def main():
    n = int(input())
    for i in range(n):
        line = input()
        print(encode(line))

main()