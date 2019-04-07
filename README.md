# Solutions to Code Jam 2019

This repository contains my solutions to the Code Jam problems from 2019. I mostly participate to get better at this sort of problems.

## Qualification Round 2019

### Forgone Solution
[Google Code Jam Problem - Forgone Solution](https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/0000000000088231)

My approach here is pretty simple. I convert the integer to a list of the digits in reverse and call this `a`, then I make another list of zeroes that has the same length and call it `b`. I then go through each digit of `a`. If I see a `4` I check which index `i` we're at and subtract one from that index in `a` and add one to that index in `b` such that `a[i] = a[i]-1` and `b[i] = b[i]+1`. After I've run through all the digits, I reverse the lists and convert them to integers. I now have two integers not containing any `4`s, but still add up to the same number given as input.

My implementation of the algorithm passed all the test sets.

### You Can Go Your Own Way
[Google Code Jam Problem - You Can Go Your Own Way](https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da)

This implementation might be a bit naive, but it passed all the test cases. We start by setting our preferred move, which is the move we will always take, unless Lydia gets in our way. This will always be the same as Lydia's last move. The reasoning behind this is, that if Lydia's last move is `S`, then if we're already at the southern edge of the maze, we can only make the move `E`, and we already know that Lydia wont get in our way.

So we just keep going until we reach the edge, then go in the other direction. Only diverging when intersecting with Lydia's path. We keep track of this by maintaining a tuple of current coordinates for ourselves and Lydia.

### Cryptopangrams
[Google Code Jam Problem - Cryptopangrams](https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/000000000008830b)

I spent more time on this than I would like to admit, but in the end I think I found a pretty nifty solution. First of all I implemented a function to find greatest common divisor of two numbers using the Euclidean algorithm.

We then looked through the cipher-text until reaching two different ciphers. We need two different semi primes to find their common divisor, otherwise it would just be itself. Since we at this point know one factor of two semi primes, we can easily find their other factor by dividing the semi prime by gcd. This other factor is then used in the previous cipher and by using the same method as before we can find the previous ciphers other factor. We do this iteratively until we reach the beginning of the cipher-text. We then reverse this list and append each element to our final list of primes.

We then go forward from the point where we first found two distinct ciphers, and use the same strategy that we used to go backwards but just appending the primes directly to our final list of primes. This list is saved for later.

We then make another list, but remove all duplicate primes from it, sort it from lowest to highest prime, then run through it, assigning each prime to an uppercase letter starting with the lowest prime assigned to `A` the second assigned to `B` with the last assigned to `Z`.

We then call our decipher function which takes the final list of primes along with the dictionary just described, and looks up each prime in the dictionary replacing them with a letter. The encrypting scheme has now been broken.

### Dat Bae
[Google Code Jam Problem - You Can Go Your Own Way](https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881de)

I didn't have the time to get a proper look at this exercise.