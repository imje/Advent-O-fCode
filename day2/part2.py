the_power = 0


def replace(line_text):
    what_to_replace = ';:'
    for i in what_to_replace:
        if i in line_text:
            line_text = line_text.replace(i, ',')
    line_text = line_text.replace(' ', '')
    return line_text

def isNumber(entry):
    full_number = ''
    for i in entry:
        if i.isdigit():
            full_number += i
    return int(full_number)

#sjekk game for game
with open('input.txt') as f:
    for line in f:
        is_ok = True
        reds = []
        blues = []
        greens = []
        x = replace(line).split(',')

#finner alle av hver farge
        for i in x:
            if ('red' in i):
                reds.append(isNumber(i))
            if ('green' in i):
                greens.append(isNumber(i))
            if ('blue' in i):
                blues.append(isNumber(i))
        
        the_power += (max(blues)*max(greens)*max(reds))
        
print(the_power)
