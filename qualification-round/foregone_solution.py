def convert_to_nonreversed_int(ls):
    return int("".join(map(str, list(reversed(ls)))))

def get_two_checks(n):
    a = list(map(int, n))
    a = list(reversed(a))
    b = [0] * len(a)

    for index, digit in enumerate(a):
        if digit == 4:
            a[index] -= 1
            b[index] += 1

    result_a = convert_to_nonreversed_int(a)
    result_b = convert_to_nonreversed_int(b)

    return (result_a, result_b)

if __name__ == '__main__':

    num_of_testcases = int(input())

    for i in range(num_of_testcases):
        n = input()
        result_a, result_b = get_two_checks(n)

        print('Case #'+str(i+1)+':', result_a, result_b)