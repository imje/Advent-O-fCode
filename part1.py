total = 0
linjenummer = []

with open('input.txt') as f:
    for line in f:
        for i in line:
            if i.isdigit():
                linjenummer += i
        total += int(linjenummer[0]+linjenummer[len(linjenummer)-1])
        linjenummer = []

print(total)