import math


def create_file(file_path, row_num):
    """
    Create source file with rows

    :param file_path:
    :param row_num:
    :return:
    """
    with open(file_path, 'w') as s:
        for i in range(1, row_num + 1):
            s.write('row ' + str(i) + " \n")


def is_perfect_square(x):
    """
    Square number, a number which is the square of an integer

    :param x:
    :return:
    """
    s = int(math.sqrt(x))
    return s * s == x


def is_fibonacci(n):
    """
    n is Fibonacci if one of 5*n*n + 4 or 5*n*n - 4 or both
    is a perfect square
    """
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)


def create_output(file_path, file_path_result):
    with open(file_path, 'r') as s:
        with open(file_path_result, 'w') as out:
            for i in s:
                y = i.split(" ")
                if is_fibonacci(int(y[1])):
                    # reversing a string before adding in output.txt
                    out.writelines(i[::-1])


def main():
    file_path = 'source.txt'
    file_path_result = 'output.txt'
    row_nums = 10
    create_file(file_path, row_nums)
    create_output(file_path, file_path_result)


if __name__ == "__main__":
    main()
