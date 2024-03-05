from functools import reduce

# 1. Map
def quadratic_func(num: tuple) -> int:
    return num[0]*num[0] + 2*num[1] + num[2]

# 2. Filter
def filter_adults(record: tuple) -> bool:
    return record[1] >= 18

# 3. Reduce
def sum(a: int, b: int) -> int:
    return a + b

if __name__ == '__main__':

    # 1. Map
    nums = [(1,2,3),(4,5,6),(7,8,9)]

    # returns map object over which we can iterate
    nums1 = map(quadratic_func, nums)

    # or we can simply convert map object to list
    print(*list(nums1))

    nums2 = list(map(lambda x: x[0]*x[0] + 2*x[1] + x[2], nums))
    print(*nums2)


    # 2. Filter
    records = [("Anand", 24), ("Rahul", 27), ("Aditya", 16), ("Neeraj", 26)]
    adults = filter(filter_adults, records)
    print(*list(adults))


    # 3. Reduce
    numbers = [1,2,3,4,5,6,7,8,9,10]
    sum_numbers = reduce(sum, numbers)

    sum_numbers2 = reduce(lambda x,y : x + y, numbers)
    print(sum_numbers2)


    # Question 1: Combine Map Reduce & Filter
    # Given a list, calculate sum of squares of all even numbers
    output = reduce(lambda x,y: x + y, map(lambda x: x*x, filter(lambda x: x % 2 == 0, numbers)))
    print(output)

    # Question 2: Frequency of words using Map/Reduce/Filter
    words = ['hello','micron','anand','ram','ram','ram','micron','iiitd','iiitd','iiitd']

    # 2a: Using dictionary comprehension
    frequency = {word: words.count(word) for word in words}

    sorted_frequency = sorted(frequency.items(), key = lambda x: x[1])
    print(sorted_frequency)

    # 2b: Using Map/Filter/Reduce
    reduce(lambda x,y: (x[0], x[1]+y[1]) if x[0] == y[0] else () ,map(lambda word: (word, 1), words))

