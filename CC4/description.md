# CC4 - Slacker Optimizations

## Introduction

![](images/books.jpg)

In an alternate reality, Zosha lives in the mountains with her hundreds of dogs and is a student at 
a local university. Her most recent assignment is to write a report on a book of her choice. Zosha is
not fond of reading and wants to choose the shortest book possible so she can spend time with her 
dogs instead.

Despite her distaste for reading, Zosha has many books to choose from in her home. She has been 
collecting them and arranging them around her house to make herself seem more sophisticated. 
Unfortunately, her books are extremely disorganized and scattered around the house in various 
piles. Looking for the shortest book may take longer than reading one!

Help Zosha find the pile with the shortest book by keeping track of the minimum length book in a
pile of books!

## Challenge

#### Overview
You will design a data structure that acts as a pile of books and keeps track of the shortest
book in the pile at any state.  

Your data structure should hold all of the books in the pile and allow for them to be inserted and
removed. 

Insertion and removal should operate in such a way that the last book added to the pile is the first
to be removed. 

The books inserted and removed from this data structure will be represented by integer values that 
indicate a book's number of pages, or length. No additional information is needed about the books 
for this data structure so you can think of a book as a number of pages.

This data structure should be defined by a class, Books, and should support the functions insert, 
remove, and shortest_book as defined below. 

A template class has been provided, but all required functions need to be added. 
Feel free to use as many member functions and class attributes as needed. 

#### Specs

- **insert(book)**
    - Given a book, add it to the pile.
    - book: int value representing the books length.
    - return: None
    - Time Complexity: O(1)

- **remove()**
    - Remove the book that was most recently added to the pile.
    - return: int value representing the book removed. Returns None if pile empty.
    - Time Complexity: O(1)
    
- **shorted_book()**
    - Returns the shortest book in the pile. 
    - return: int value representing the shortest book. Returns None if pile empty.
    - Time Complexity: O(1)

#### Complexity

All functions must operate in constant time - O(1). *Extra credit for space complexity of O(1).*
This would require no additional space to be used except the books themselves.

#### Examples

A list will be used to represent a pile of books in the following examples.


Before adding anything, the pile is empty.

[]

Add a book of size 2 to the pile.

[2]

The shortest book is 2 pages.

Add a book of size 3 to the pile.

[2, 3]

The shortest book is 2 pages.

Add a book of size 1 to the pile.

[2, 3, 1]

The shortest book is 1 page. 

Remove a book from the pile.

[2, 3]

1 is removed and returned.

The shortest book is 2 pages.

Remove a book from the pile.

[2]

3 is removed and returned.

The shortest book is 2 pages.

Remove a book from the pile.

[]

2 is removed and returned.

The shortest book in the pile is None.


#### Guarantees

- Only non-negative integer values will be inserted and removed from Books.

## Submission

#### Deliverables

Be sure to upload the following deliverables in a .zip folder to Mimir by 8:00pm 
Eastern Time on Thursday, 10/15/2020.

Your .zip folder can contain other files (for example, `description.md` and `tests.py`), but must include
(at least) the following:

    CC4.zip
        |— CC4/
            |— README.md        (for coding challenge feedback)
            |— __init__.py      (for proper Mimir testcase loading)
            |— solution.py      (contains your solution source code)
            
#### Grading

The following 100-point rubric will be used to determine your grade on CC2:

- Tests (75)
    - 00 - Coding Standard: __/5
    - 01 - Test Basic: __/13
    - 02 - Test Empty: __/13
    - 03 - Test Duplicates: __/13
    - 04 - Test Small Random: __/13
    - 05 - Test Large Random: __/18
- Manual (25)
    - Time Complexity is *O(1)*: __/20
    - README.md is *completely* filled out with (1) Name, (2) Feedback, (3) Time
    to Completion and (4) Citations: __/5
    - Extra Credit for Space Complexity *O(1)*: __/10
        
## Tips, Tricks & Notes

- *You must fill out docstrings to receive Coding Standard points.*
- Additional data structures other than Python List are not allowed.
- List append() operates in O(1)
- List pop() (when used on the last element in a list) operates in O(1)
