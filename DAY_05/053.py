# Calclate sum of even numbers from 0 to 100

total_of_even = 0;
# Method : 1
for even_num in range(0, 101, 2):
    total_of_even += even_num
print(total_of_even)



# Method : 2
total_of_even = 0;
for even_num in range(0, 101):
    if even_num % 2 == 0:
        total_of_even += even_num
print(total_of_even)

