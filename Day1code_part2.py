nummer = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}

number_dict = {}
total = 0

with open('/Users/ingvild/kode/AdventCalendar/Day1/input.txt') as f:
    for line in f:
        for i in line:
            if i.isdigit():
                number_dict[line.rfind(i)] = i

        #finne str
        for i in nummer:
            if i in line:
                number_dict[line.rfind(i)] = nummer[i]
    
#lage en dictionary og sortere den etter hvilket tall som kommer først og sist

        sorted_dict = dict(sorted(number_dict.items()))
        print(sorted_dict)
        print(list(sorted_dict.values())[0])
        print(list(sorted_dict.values())[len(sorted_dict)-1])
        total += int(list(sorted_dict.values())[0]+list(sorted_dict.values())[len(sorted_dict)-1])
        print(total)
        number_dict = {}

print(total)