# CC3 - Dinner Time!

## Introduction

![](images/dogs.jpg)

In an alternate reality, Zosha lives in the mountains where she cares for her hundreds of rescued dogs. She takes 
very good care of them, taking them on long walks and giving them lots of treats. She loves her pups, but keeping 
track of them all can be quite the challenge!

She is facing a strange reoccurring problem and needs your help!

At dinner time, she prepares a bowl of kibble for exactly every dog.
After she calls all of the dogs in for dinner, she always notices exactly one bowl not eaten. 
She has a list of all of the dogs who attended dinner, but doesn't have enough time to read through it and determine
which dog is missing.

In this coding challenge, you will be helping Zosha identify the hungry dog! 
Luckily, all of her dogs were given integer ids in sequential order, so you will be tasked with identifying the missing 
id number in a sequential list.

## Challenge

#### Overview

Given a list of sequential integers (starting from 0), find the missing number. 

More formally, you will be given a list of n integers in the range of 0 to n. There are no duplicates in the list. 
One of the integers is missing in the list. Write a recursive algorithm to identify the missing number.

An empty inner function has been provided and is **required to be used recursively in the solution**.

To receive full credit for your solution, your algorithm must be recursive and you must adhere to a time complexity 
of *O(log(n))*.

#### Input

- A `list` of size n containing numbers in the range of 0 to n.

#### Output

- An `int` representing the missing number.

#### Complexity

For an input of size n, you must adhere to a time complexity of *O(log(n))* and a space complexity of *O(1)*.

#### Examples

- The number 3 is missing from the range 0 to 5.

    Input: [0, 1, 2, 4, 5]

    Output: 3



- The number 6 is missing from the range 0 to 9.

    Input: [0, 1, 2, 3, 4, 5, 7, 8, 9]
    
    Output: 6



- The number 0 is missing from the range 0 to 7.

    Input: [1, 2, 3, 4, 5, 6]
    
    Output: 0



- The number 1 is missing from the range 0 to 1.

    Input: [0]
    
    Output: 1



- The number 0 is missing from the range 0 to 0.

    Input: []
    
    Output: 0


#### Guarantees

- The range will start from 0.
- There will always be a missing number.
- Numbers will always be sorted in increasing order.

## Submission

#### Deliverables

Be sure to upload the following deliverables in a .zip folder to Mimir by 8:00p 
Eastern Time on Thursday, 10/01/2020.

Your .zip folder can contain other files (for example, `description.md` and `tests.py`), but must include
(at least) the following:

    CC3.zip
        |— CC3/
            |— README.md        (for coding challenge feedback)
            |— __init__.py      (for proper Mimir testcase loading)
            |— solution.py      (contains your solution source code)
            
#### Grading

The following 100-point rubric will be used to determine your grade on CC2:

- Tests (75)
    - 00 - Coding Standard: __/5
    - 01 - Test Basic: __/10
    - 02 - Test Missing First: __/10
    - 03 - Test Missing Last: __/10
    - 04 - Test Small Sequence: __/20
    - 05 - Test Large Sequence: __/20
- Manual (25)
    - Time Complexity is *O(log(n))*: __/20
    - README.md is *completely* filled out with (1) Name, (2) Feedback, (3) Time
    to Completion and (4) Citations: __/5
        
## Tips, Tricks & Notes

- *You must fill out docstrings to receive Coding Standard points.*
- The inner function can be used to access indices for sub-sequences during recursion.
- Only the inner function is required to be used recursively.
- You may not use any additional data structures.
- Hint: Compare values to their index.
- Hint: Think of a binary search 

