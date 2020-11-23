
# :books: 0x00-arrays_practice 

## Task:pencil:
<br>

:zero: [Merge ranges]()

Write a function merge_ranges() that takes a list of multiple meeting time ranges and returns a list of condensed ranges.
For example, given: 

```[(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]```

your function would return:

``` [(0, 1), (3, 8), (9, 12)]```



:one: [Reverse a list of chars]()

Write a function that takes a list of characters and reverses the letters in place.

:two: [reverse a list of words ]()

Write a function reverse_words() that takes a message as a list of characters and reverses the order of the words in place. 

For example: 

    message = [ 'c', 'a', 'k', 'e', ' ',
                'p', 'o', 'u', 'n', 'd', ' ',
                's', 't', 'e', 'a', 'l' ]

    reverse_words(message)

    # Prints: 'steal pound cake'
    print(''.join(message))


:three: [Merge two sorted arrays]()

Write a function to merge our lists of orders into one sorted list. 

Example

    my_list     = [3, 4, 6, 10, 11, 15]
    other_list = [1, 5, 8, 12, 14, 19]

    # Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
    print(merge_lists(my_list, other_list))

:four: [First come, first served]()

Given all three lists, write a function to check that my service is first-come, first-served. All food should come out in the same order customers requested it


The take-out orders as they were entered into the system and given to the kitchen. (take_out_orders)
The dine-in orders as they were entered into the system and given to the kitchen. (dine_in_orders)
Each customer order (from either register) as it was finished by the kitchen. (served_orders)

 As an example
 
    Take Out Orders: [1, 3, 5]
    Dine In Orders: [2, 4, 6]
    Served Orders: [1, 2, 4, 6, 5, 3]

