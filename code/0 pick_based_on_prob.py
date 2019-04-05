# -*- coding: utf-8 -*-
"""Given an array with each element has a probability, choose one element according to its probability.

0.1 Giant array pool method
    step 1: Generate a new array by repeating the each element for multiple times according to its probability.
    step 2: Randomly pick one from the array.

0.2 Accept/Rejection method
    step 1: Randomly pick one element.
    step 2: Get a random float number from 0 to 1.
        If the number is less than the probability of the element, accept this element and return it.
        Else back to step 1 to pick again.

0.3 Bar method (RECOMMENDED)
    step 1: Set default picked element is the first element.
    step 1: Get a random float number (r) form 0 to 1.
    step 2: While r is greater than 0
        r = r - probability of picked element
        picked element index ++
    step 3: return picked element
"""
import random, time
from pprint import pprint

def pick_one_by_giant_array_pool(array):
    giant_array = [elem for elem in array for i in range(elem['score'])]
    picked_index = random.randint(0, len(giant_array)-1)
    return giant_array[picked_index]

def pick_one_by_accept_rejection(array):
    while True:
        picked_index = random.randint(0, len(array)-1)
        r = random.random()
        if r < array[picked_index]['prob']:
            return array[picked_index]

def pick_one_by_bar_method(array):
    picked_index = 0
    r = random.random()
    while r > 0:
        r -= array[picked_index]['prob']
        picked_index += 1
    picked_index -= 1
    return array[picked_index]

def test(N, array, pick_func):
    """Pick for N times, and count distribution of each element.
    """
    # Initialize the array by adding vars of 'count' and 'prob'.
    sum = 0
    for elem in array:
        sum += elem['score']
    for elem in array:
        elem['count'] = 0
        elem['prob'] = float('%.4f' %(elem['score'] / sum))
    # Pick
    for i in range(N):
        elem = pick_func(array)
        elem['count'] += 1
    return array


if __name__=="__main__":
    fruits = [
        {"name":"mango", "score":5},
        {"name":"blueberry", "score":3},
        {"name":"cherry", "score":1},
        {"name":"banana", "score":7},
        {"name":"apple", "score":1},
    ]
    pick_func_list = [
        pick_one_by_giant_array_pool,
        pick_one_by_accept_rejection,
        pick_one_by_bar_method
    ]
    for pick_func in pick_func_list:
        print("\nPick function: %s." %(pick_func.__name__))
        time0 = time.time()
        test(100000, fruits, pick_func)
        pprint(fruits)
        print("Costs %.4f sec." %(time.time() - time0))
