"""
Unlike list or array, generators dont store all the values in memory
which can be useful when dealing with large datasets or infinite sequences

Ex 1: 1 million elements in a list needs to be mapped to its square
Instead of creating a list of squares, we create a generator as it will not
calculate immediately and store in memory, instead will yield one by one
when we iterate

Ex 2: We want an infinite list of multiples of 5, we can't do it using list
as we dont know the size. So we create a generator that will keep on
generating the values infinitely
"""

def square_numbers_traditional(nums):
    res = []
    for num in nums:
        res.append(num*num)
    return res

def square_numbers_traditional_list_compr(nums):
    return [num*num for num in nums]

def square_nums_generator(nums):
    for num in nums:
        yield num*num

def square_nums_generator_list_compr(nums):
    # when we use brackets instead of square brackets
    # we create a GENERATOR INSTEAD OF A LIST
    return (num*num for num in nums)

if __name__ == '__main__':
    nums = [1,2,3,4,5]
    print(square_numbers_traditional(nums))
    print(square_numbers_traditional_list_compr(nums))

    # Both of the following return generator objects
    gen1 = square_nums_generator(nums)
    gen2 = square_nums_generator_list_compr(nums)
    gen3 = square_nums_generator(nums)

    try:
        while True:
            # yield element 1 by 1 from gen1 generator object
            print(next(gen1))
    except StopIteration:
        print("Finished printing all elements from generator 1")


    # Prints list elements as usual
    for num in gen2:
        print(num)

    # Will not print anything since we
    # ALREADY CONSUMED the elements above
    for num in gen2:
        print(num)

    # Converts the generator to a list and prints
    # Don't get benefit of generators
    print(list(gen3))



    l1 = [1,2,3,4]
    l2 = [5,6,7,8]

    # Bad way of writing
    for i in range(len(l1)):
        print(l1[i])
        print(l2[i])
        # do something with i

    # Better way
    for i, (a,b) in enumerate(zip(l1,l2)):
        print(a,b)
        # do something with i

    # If no need to use i
    for (a,b) in zip(l1,l2):
        print(a)
        print(b)