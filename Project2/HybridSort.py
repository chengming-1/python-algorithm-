"""
Name:Chengming Wang
Project 2 - Hybrid Sorting - Starter Code
CSE 331 Fall 2020
Professor Sebnem Onsay
"""

from typing import List, Any, Dict


def insertion_sort(data):
    """
    :param data：list
    :return: the sorted num
    """
    for i in data:
        j = data.index(i)
        while j > 0:
            if data[j - 1] > data[j]:
                data[j - 1], data[j] = data[j], data[j - 1]
            else:
                break
            j = j - 1


def hybrid_sort(data, threshold):
    """
    :param data: list
    :return: none
    return to other function by choosing
    """
    if threshold == 0:
        temp_arr = [0] * len(data)
        return inversion_count(data, temp_arr, 0, len(data) - 1)
    return insertion_sort(data)


def inversion_count(data, temp_arr, left, right):
    """
    :param data:list
    :param temp_arr: temp list
    :param left: the small num
    :param right: the big num
    :return: the lacking number
    """
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += inversion_count(data, temp_arr, left, mid)
        inv_count += inversion_count(data, temp_arr, mid + 1, right)
        inv_count += merge(data, temp_arr, left, mid, right)
    return inv_count


def merge(data, temp_arr, left, mid, right):
    """
    :param data:list
    :param temp_arr: temp list
    :param left: the small num
    :param mid: the middle one (left+right//2)
    :param right: the big num
    :return: the lacking number
    """
    i = left
    j = mid + 1
    k = left
    inv_count = 0
    while i <= mid and j <= right:
        if data[i] <= data[j]:
            temp_arr[k] = data[i]
            k += 1
            i += 1
        else:
            temp_arr[k] = data[j]
            inv_count += (mid - i + 1)
            k += 1
            j += 1
    while i <= mid:
        temp_arr[k] = data[i]
        k += 1
        i += 1
    while j <= right:
        temp_arr[k] = data[j]
        k += 1
        j += 1
    for loop_var in range(left, right + 1):
        data[loop_var] = temp_arr[loop_var]
    return inv_count


def merge_sort(list):
    """
    :param myList:list
    """
    inv_count = []
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1
            inv_count.append(1)
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
            inv_count.append(1)
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
            inv_count.append(1)


def inversions_count(data):
    """
    :param data:list
    """
    leng = len(data)
    arr = data
    inv_count = 0
    for i in range(leng):
        for j in range(i + 1, leng):
            if arr[i] > arr[j]:
                inv_count += 1
    return inv_count


def find_match(user_interests, candidate_interests):
    """
    :param user_interests: total variable
    :param candidate_interests: user own variable
    """
    key_list = []
    result_list = []
    data1 = user_interests
    result_user = abs(inversion_count(data1, [0] * len(data1), 0, len(data1) - 1))
    for key in candidate_interests:
        key_list.append(key)
        data = candidate_interests[key]
        result = inversion_count(data, [0] * len(data), 0, len(data) - 1)
        result -= result_user
        result_list.append(result)
    final_key_index = result_list.index(min(result_list))
    final_key = key_list[final_key_index]
    return final_key
