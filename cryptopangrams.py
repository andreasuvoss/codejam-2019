def integer_sqrt(n):
    x = n
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def fermat(n):
    a = integer_sqrt(n)
    b2 = a * a - n
    b = integer_sqrt(n)

    while b * b != b2:
        a += 1
        b2 = a * a - n
        b = integer_sqrt(b2)

    return (a+b, a-b) 

def decipher(prime_string, dictionary):
    plaintext = []
    plaintext = list(map(lambda prime: dictionary[prime], prime_string))
    return (''.join(plaintext)).upper()

if __name__ == '__main__':

    num_testcases = int(input('Number of tests: '))

    primes = []

    for i in range(num_testcases):
        max_prime, num_chars = tuple(map(int, input().split(' ')))
        ciphertext = list(map(int, input().split(' ')))

        # We factor the first semiprime in the ciphertext
        first = fermat(ciphertext[0])
        dictionary = {}

        # We now know that one of the numbers in first is used to create the semiprime for second.
        prime_in_next = 0
        if ciphertext[1] % first[0] == 0:
            primes.append(first[1])
            prime_in_next = ciphertext[1] / first[0]
            primes.append(first[0])
        else:
            primes.append(first[0])
            prime_in_next = ciphertext[1] / first[1]
            primes.append(first[1])

        for j in range(2, len(ciphertext)):
            primes.append(prime_in_next)
            prime_in_next = ciphertext[j] / prime_in_next
        
        primes.append(prime_in_next)

        primes = list(map(int, primes))

        #print(primes)

        #print(sorted(set(primes)))

        for index, prime in enumerate(sorted(set(primes))):
            dictionary[prime] = chr(97 + index)

        #print(dictionary)
        #print(primes)

        print(primes)
        print('Case #'+str(i+1)+':', decipher(primes, dictionary))

