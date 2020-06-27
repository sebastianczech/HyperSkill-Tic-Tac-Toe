prime_numbers = [k for k in range(1001) if k > 1 and all(k % i != 0 for i in range(2, k - 1))]
