data = input()

result = []

if data[0] == 'E':
    result.append('I')
else:
    result.append('E')

if data[1] == 'S':
    result.append('N')
else:
    result.append('S')

if data[2] == 'T':
    result.append('F')
else:
    result.append('T')

if data[3] == 'J':
    result.append('P')
else:
    result.append('J')

for i in result:
    print(i, end = "")