# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    result_score = [0,0,0, 0,0,0, 0,1,0, 0,0,0]
    result_type = 0

    if result_score[3] == 1 or (result_score[4] == 1 and result_score[5] == 1):
        result_type = 2
        if result_score[6] == 1 or (result_score[7] == 1 and result_score[8] == 1):
            result_type = 3
            if result_score[9] == 1 or (result_score[10] == 1 and result_score[11] == 1):
                result_type = 4
    else:
        result_type = 1

    print(result_type)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

