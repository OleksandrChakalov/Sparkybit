import math

def create_file(file_path, row_num):
    """
    Create output file with rows

    :param file_path:
    :param row_num:
    :return:
    """
    with open(file_path, 'w') as s:
        for i in range(1, row_num + 1):
            s.write('row ' + str(i) + '\n')


def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x

def isFibonacci(n):
    """
    n is Fibonacci if one of 5*n*n + 4 or 5*n*n - 4 or both
    is a perfect square
    """
    return isPerfectSquare(5 * n * n + 4) or isPerfectSquare(5 * n * n - 4)












def main():
    file_path = 'source.txt'
    row_nums = 10
    create_file(file_path, row_nums)


if __name__ == "__main__":
    main()
