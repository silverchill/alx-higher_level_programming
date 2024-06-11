#!/usr/bin/python3
""" module that finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):

    """ function that finds a peak in a list of unsorted integers """
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
