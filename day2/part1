max_red = 12
max_green = 13
max_blue = 14

sum_of_id = 0


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
        x = replace(line).split(',')

#summer rød, grønn, blå hver for seg og sjekk de opp mot max
        for i in x:
            if ('red' in i) and (isNumber(i) > max_red):
                is_ok = False
            if ('green' in i) and (isNumber(i) > max_green):
                is_ok = False
            if ('blue' in i) and (isNumber(i) > max_blue):
                is_ok = False
    
        if is_ok == True:
            sum_of_id += isNumber(x[0]) 
        

print('summen', sum_of_id)
