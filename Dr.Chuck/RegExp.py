import re
txt = open('regex_sum_274477.txt', 'r')
sum = 0

for line in txt:
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        sum = sum + int(number)

print (sum)
