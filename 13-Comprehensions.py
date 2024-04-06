"""
Python offers 4 types of comprehension:
List, Dictionary, Set, Generator
"""

if __name__ == '__main__':

    # 1. List comprehension
    nums = [1,2,3,4,5,6]
    squared_nums = [n*n for n in nums]
    square_odd_nums = [n*n for n in nums if n % 2 == 0]  # if condition comes in the end

    matrix = [[1,-2,3],[-6,6,4],[3,-1,2]]
    flat_positive_matrix = [y for x in matrix for y in x if y >= 0] # nested for loop is written in order
    print(flat_positive_matrix)

    names = ['Bruce','Clark','Peter','Logan','Wade']
    heros = ['Batman','Superman','Spiderman','Wolverine','Deadpool']

    # create pair of name and hero (name,hero)
    named_heroes = [(name,hero) for name, hero in zip(names,heros)]
    print(named_heroes) #[('Bruce', 'Batman'), ('Clark', 'Superman'),....


    sentence = 'Those Woofers Im shit scared of that sHit Scared OF A SHIT Scared oF B'
    cnt_lower = sum(1 for c in sentence if c.islower())
    cnt_upper = sum(1 for c in sentence if c.isupper())
    print('Count of lowercase: ',cnt_lower,', Count of uppercase: ',cnt_upper)

    # 2. Dictionary comprehension

    # create dictionry of name as key hero as value
    named_heroes = {name: hero for name, hero in zip(names,heros)}
    print(named_heroes)  #{'Bruce': 'Batman', 'Clark': 'Superman', 'Peter':...


    # 3. Set comprehension
    nums = [1,2,3,3,3,3,4,4,6,6]
    distinct_nums = {num for num in nums}
    print(distinct_nums)

    # 4. Generator comprehension
    nums = [1,2,3,4,5,6]
    my_gen = (num*num for num in nums)
    for x in my_gen:
        print(x, end=',')