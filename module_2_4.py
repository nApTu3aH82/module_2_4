numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for check_num in numbers:
    if check_num == 1:
        continue
    is_prime = True
    for i in range(2, check_num):
        if check_num % i == 0 and check_num != 2:
            is_prime = False
            break
    if is_prime == True:
        primes.append(check_num)
    else:
        not_primes.append(check_num)
print(primes)
print(not_primes)
