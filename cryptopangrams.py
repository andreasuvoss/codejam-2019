def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def decipher(prime_string, dictionary):
    plaintext = []
    plaintext = list(map(lambda prime: dictionary[prime], prime_string))
    return (''.join(plaintext)).upper()

if __name__ == '__main__':

    num_testcases = int(input())

    for tc in range(num_testcases):
        max_prime, num_chars = tuple(map(int, input().split(' ')))
        ciphertext = list(map(int, input().split(' ')))

        primes = []
        dictionary = {}
        
        # We find greatest common divisor between the first two ciphers that are different.
        j = 0
        while ciphertext[j] == ciphertext[j+1]:
            j += 1    
        
        gcd_first_two = gcd(ciphertext[j], ciphertext[j+1])
        first = (int(ciphertext[j] // gcd_first_two), gcd_first_two)

        if j != 0:
            prime_in_prev = int(ciphertext[j] // gcd_first_two)
            temp_prime = []

            # We know that GCD is also used to create the semiprime for second.
            for i in range(j):
                if i != 0:
                    temp_prime.append(prime_in_prev)
                prime_in_prev = ciphertext[j-i] // prime_in_prev

            temp_prime.append(prime_in_prev)

            for prime in reversed(temp_prime):
                primes.append(prime)

        primes.append(first[0])
        prime_in_next = gcd_first_two

        for i in range(j+1, len(ciphertext)):
            primes.append(prime_in_next)
            prime_in_next = int(ciphertext[i] // prime_in_next)

        primes.append(prime_in_next)

        primes = list(map(int, primes))

        for index, prime in enumerate(sorted(set(primes))):
            dictionary[prime] = chr(97 + index)

        print('Case #'+str(tc+1)+':', decipher(primes, dictionary))