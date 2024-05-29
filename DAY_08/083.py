def prime_checker(number):
    is_prime = True
    # if number == 2 or number == 1:
    #     print("Prime")
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime == True:
        print("Its a Prime Number")
    else:
        print("Its not a Prime Number")
    



n = int(input("Check this number: "))
prime_checker(number=n)