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

with open('input.txt') as f:
    for line in f:
        for i in line:
            if i.isdigit():
                number_dict[line.find(i)] = i
                number_dict[line.rfind(i)] = i

        #finne str
        for i in nummer:
            if i in line:
                number_dict[line.find(i)] = nummer[i]
                number_dict[line.rfind(i)] = nummer[i]
    
        sorted_dict = dict(sorted(number_dict.items()))
        total += int(list(sorted_dict.values())[0]+list(sorted_dict.values())[len(sorted_dict)-1])
        number_dict = {}

print(total)
