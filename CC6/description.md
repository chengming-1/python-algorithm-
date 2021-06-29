##CC6 - It’s as easy as 01-10-11

**Due: Thursday, November 12th @ 8:00pm**

**This is not a team project, do not copy someone else’s work.**

###Introduction

Alien robots have come from Mars and abducted Angelo. He is panicking because he still needs to do his CSE project, so he needs to get back as soon as possible. Too bad he can’t communicate with the aliens! If he was able to tell them, surely they would understand.

He manages to report that they seem to communicate using binary. He proposes that we convert all of our alphabets and languages into binary, so that we can talk to them. We need you to write a binary converter that can generate these binary representations based on how many characters are in an alphabet.

###Challenge
####Overview

In this challenge, you will be implementing a queue and a binary generator. **This means that using a python generator is required.** This function takes a value n and converts every number from 0 to n (inclusive) into binary. Be careful, however! Not all input is guaranteed to be valid.

Recall: 
- A queue is a data structure following a first-in first-out (FIFO) ordering of removal
- Queues have runtime of O(1) for both insert and removal. We are using a linked list based queue, not array based. So runtime is not amortized.
- For more information, look at zybooks or your lecture slides

**Class Node:**

This class is given to you to use in the queue.

- **Attributes**
    - **value**: the value of the node 
    - **next**: reference to the node immediately following this node
- **__init__(self, value)**:
    - **value**: the value to be saved to this node (string)
    - Constructs an instance of a Node in the queue
    - Time Complexity: O(1)
    - Space Complexity: O(1)
- **__str__(self)**:
    - Constructs a string representation of the node

**Class Queue:**

The following is given as a guide to you. Feel free to change the class definition as you see fit.

- **Attributes**:
    - **first**: Node at the start of the queue
    - **last**: Node at the end of the queue
- **__init__(self)**
    - Constructs a queue with the first and last node initialized at None
- **__str__(self)**
    - Constructs a string representation of the queue

_IMPLEMENT the following functions:_

- **insert(self, value)**
    - **value**: value of type string to be added into the queue as a Node
    - Inserts value into the queue at the end of the queue
    - Return: **None**
    - Time Complexity: O(1)
    - Space Complexity: O(1)
- **pop(self)**
    - Removes the first element in a queue
    - Return: **value of the removed node**
    - Time Complexity: O(1)
    - Space Complexity: O(1)

**alien_communicator(n)**
- **n**: any built-in type in python (i.e. sets, dictionaries, strings, etc.)
- If n is an int, return all binary numbers of zero to n inclusive -> [0, n]
- If n is not an integer, **return None**
- Return: **generator object containing string representations of binary numbers 0 through n inclusive**

####Complexity

Time Complexity: **O(n)** where n is the size of the input.
E.G. N = 10 in binary_converter(10)

Space Complexity: **O(n)** auxiliary space where n is the size of the input (see above).
This does not count space allocated on any call stacks.

####Examples

_The output is shown as a list here, but will be a generator object when you return your code's output._

n = 0

output:   **['0']**

decimal:   0




n = {}  --> This is an empty dictionary

output:   **[]**




n = 3

output:   **['0', '1', '10', '11']**

decimal:   0    1    2     3




n = 16

output:   **['0', '1', '10', '11', '100', '101', '110', '111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111', '10000']**

decimal:   0    1    2     3      4      5       6      7       8         9        10        11       12       13      14       15        16




### Submission
#### Deliverables

Be sure to upload the following deliverables in a .zip folder to Mimir by 8:00p Eastern Time on Thursday, 11/12/20.

    CC6.zip
        |— CC6/
            |— README.md       (for coding challenge feedback)
            |— __init__.py     (for proper Mimir testcase loading)
            |— solution.py     (contains your solution source code)

#### Grading

The following 100-point rubric will be used to determine your grade on CC6:

- Tests (75)
    - 00 - Coding Standard: __/5
    - 01 - Zero: __/2
    - 02 - Invalid Input: __/8
    - 03 - Basic: __/10
    - 04 - Even Numbers and Inputs: __/15
    - 05 - Odd Numbers and Inputs: __/15
    - 06 - Large Inputs: __/20
- Manual (25)
    - Time Complexity is O(n): __/15
    - Space Complexity is O(n): __/5
    - README.md is _completely filled out_ with (1) Name, (2) Feedback, (3) Time to Completion and (4) Citations: __/5

### Tips, Tricks, & Notes
- The use of the bin() function is not allowed whatsoever. Even if bin() were allowed, it exceeds the time complexity of O(n) too since to convert a number into binary, you must divide the number by 2 until the quotient is 0, producting an O(logn) time. By doing this for n numbers, it now runs in O(nlogn) time.
- Remember that only auxiliary space is counted towards the space complexity, meaning you can store up to n numbers before additional space gets counted against you. Since the space complexity is O(n), the maximum number of entities you can store are 2n entities.
- Remember that when you iterate over n strings with k characters your time complexity is O(kn) NOT O(n).
- **NOTE**: string concatenation is technically O(k) with k being the number of characters in the string. However, this happens in the background and we will not consider it in your time complexity. **Any manual iterations over any string will be counted in your time complexity calculations** (i.e. you do a for-loop over every character in a string).

Coding challenge designed by Angelo Savich and Olivia Mikola