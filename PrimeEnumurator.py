def calc_prime_num(a):
    n_list = range(2, a + 1)

    for i in range(2, int(a ** 0.5) + 1):
        n_list = [x for x in n_list if (x == i or x % i != 0)]

    for j in n_list:
        if j == n_list[0]:
            print(str(a) + " has " + str(len(n_list)) + " prime numbers")
            print("The prime numbers are ", end="")
        if j == n_list[-1]:
            print(j)
        else:
            print(j, end=",")


number = int(input("Enter Number: "))
calc_prime_num(number)

