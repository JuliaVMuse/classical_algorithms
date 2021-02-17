
def bubble_sort(input_list):
    """
    Bubble Sort

    :return: sorted input_list
    """

    sort = True
    n = len(input_list)
    f = 0
    while sort:
        f += 1
        sort = False
        for count_el in range(n - f):
            if input_list[count_el] > input_list[count_el + 1]:
                input_list[count_el], input_list[count_el + 1] = input_list[count_el + 1], input_list[count_el]
                sort = True

    return input_list


def selection_sort(input_list):
    """
    Selection Sort

    :return: sorted input_list
    """
    for i in range(len(input_list)):
        min = i
        for count_el in range(i + 1, len(input_list)):
            if input_list[count_el] < input_list[min]:
                min = count_el

        input_list[i], input_list[min] = input_list[min], input_list[i]
    return input_list


def insertion_sort(arr):
    """
    Insertion Sort

    :return: sorted input_list
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


def get_res(res, part_c, c_el):
    res.append(res[len(res) - 1])
    res[c_el + 1:len(res) - 1] = res[c_el:len(res) - 2]
    res[c_el] = part_c
    return res


def main_res(flag, res, part, el_, i, p):
    for el in range(p, len(res)):
        if part[0] < res[el]:
            res = get_res(res, part[i], el)
            el_ = el
            flag = False
            break
    return res, flag, el_


def appending_part(res, part):
    el_ = 0
    flag = True
    res, flag, el_ = main_res(flag, res, part, el_, 0, 0)
    if flag:
        res.append(part[0])
    if el_ == len(res):
        res.append(part[1])

    else:
        flag = True
        res, flag, el_ = main_res(flag, res, part, el_, 1, el_)
        if flag:
            res.append(part[1])
    return res


def get_parts(input_list, count_el):
    part1 = input_list[count_el:count_el + 2]
    part2 = input_list[count_el + 2:count_el + 4]

    if part1[0] > part1[1]:
        part1[0], part1[1] = part1[1], part1[0]

    if part2[0] > part2[1]:
        part2[0], part2[1] = part2[1], part2[0]
    return part1, part2


def merge_sort(input_list):
    """
    Merge Sort

    :return: sorted input_list
    """
    res = []
    number_el = 0
    for count_el in range(0, len(input_list), 4):
        if count_el + 4 < len(input_list):
            part1, part2 = get_parts(input_list, count_el)

            if len(res) == 0:
                res = part1
                res = appending_part(res, part2)

            else:
                res = appending_part(res, part1)
                res = appending_part(res, part2)
        number_el = count_el
    if number_el < len(input_list):
        for count_el in range(number_el, len(input_list)):
            for count_el1 in range(len(res)):
                if input_list[count_el] < res[count_el1]:
                    res = get_res(res, input_list[count_el], count_el1)
                    break

    return res


def quick_sort(input_list):
    """
    Quick Sort

    :return: sorted input_list
    """
    q = input_list[0]
    left_part = [n for n in input_list if n < q]
    right_part = [n for n in input_list if n > q]
    medium = [q] * input_list.count(q)

    if len(left_part) > 1:
        left_part = quick_sort(left_part)
    if len(right_part) > 1:
        right_part = quick_sort(right_part)
    return left_part + medium + right_part
