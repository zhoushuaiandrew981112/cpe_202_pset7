# Name:         Zhoushuai (Andrew) Wu
# Course:		CPE 202
# Instructor:	Daniel Kauffman
# Assignment:	Pset 7
# Term:  		Summer 2018

import random
import sys
import time


def main():
    if len(sys.argv) != 2:
        print("usage: python3 sorting.py SIZE")
        sys.exit()
    else:
        try:
            n_int = int(sys.argv[1])
        except ValueError:
            print("SIZE must be an integer")
            sys.exit()
    unsorted = [random.randint(0, 1000) for i in range(n_int)]
    goal = sorted(unsorted)
    fmt_str = ("{0:<14}: {1:>4} | {2:7.3f} Seconds | " +
               "{3:11,d} Comparisons | {4:11,d} Swaps")
    fun_dict = {"[1] Bubble": bubble_sort, "[2] Selection": selection_sort,
                "[3] Insertion": insertion_sort, "[4] Merge": merge_sort,
                "[5] Quick": quick_sort}
    for name, function in sorted(fun_dict.items(), key = lambda t: t[0]):
        list_copy = list(unsorted)
        start = time.time()
        n_comp, n_swap = function(list_copy)
        duration = time.time() - start
        status = "OK" if list_copy == goal else "FAIL"
        print(fmt_str.format(name, status, duration, n_comp, n_swap))


def bubble_sort(ints):
    c = 0
    s = 0
    for i in range(0, len(ints)):
        for j in range(0, len(ints) - i - 1):
            c += c
            if ints[j] > ints[j + 1]:
                ints[j], ints[j + 1] = ints[j + 1], ints[j]
                s += s
    return (c, s)


def selection_sort(ints):
    c = 0
    s = 0
    for i in range(0, len(ints)):
        min_i = i
        for j in range(i + 1, len(ints)):
            c += 1
            if ints[j] < ints[i]:
                min_i = j
        #s += 2
        s += 1
        ints[i], ints[min_i] = ints[min_i], ints[i]      
    return (c, s)


def insertion_sort(ints):
    c = 0
    s = 0
    for i in range(1, len(ints)):
        key = ints[i]
        j = i - 1
        while j >= 0 and key <= ints[j]:
            c += 1
            s += 1
            ints[j + 1] = ints[j]
            j -= 1
        ints[j + 1] = key
    return (c, s)


def merge_sort(ints):
    pass
    #return (0, 0)


def partition(ints, start, end):
    pivot = ints[end]
    p_i = start
    c = 0
    s = 0
    for i in range(start, end):
        c += 1
        if ints[i] <= pivot:
            s += 1
            ints[i], ints[p_i] = ints[p_i], ints[i]
            p_i += 1
    s += 1
    ints[end], ints[p_i] = ints[p_i], ints[end]
    return (p_i, c, s)


def quick_sort_helper(ints, start, end, c, s):
    if start < end:
        p_i, c, s = partition(ints, start, end)
        c_l, s_l = quick_sort_helper(ints, start, p_i - 1, c, s)
        c_r, s_r = quick_sort_helper(ints, p_i + 1, end, c, s)
        return (c + c_l + c_r, s + s_l + s_r)
    else:
        return(0, 0)


def quick_sort(ints):
    return quick_sort_helper(ints, 0, len(ints) - 1, 0, 0)


if __name__ == "__main__":
    main()
