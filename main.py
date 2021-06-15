

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


def main():
    file_path = 'source.txt'
    row_nums = 10
    create_file(file_path, row_nums)


if __name__ == "__main__":
    main()
