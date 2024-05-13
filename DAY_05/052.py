#  for loop with range

# for number in range(1, 11, 2): # starts from 1(including 1) to 11(no including 11) increment by 2 
#     print(number)   # 1 3 5 7 9

total = 0
for number in range(0, 101):
    total += number
print(total)