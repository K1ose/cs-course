# Converting iteration to recursion

def sum_below(n):
    """Sum up the integers from 1 to n-1.

    >>> sum_below(5)  # 1 + 2 + 3 + 4
    10
    """
    k = 1
    total = 0
    while k < n:
        k, total = k + 1, total + k
    return total

def sum_below_rec(n):
    """Sum up the integers from 1 to n-1.

    >>> sum_below_rec(5)  # 1 + 2 + 3 + 4
    10
    """
    def f(k, total):
        if k == n:
            return total
        else:
            return f(k + 1, total + k)
    return f(1, 0)

# Aggregation

# sum(1, 2, 3)
sum([2, 3, 4])
[2, 3] + [4]
# sum([[2, 3], [4]])
# 0 + [2, 3] + [4]
sum([[2, 3], [4]], [])
# [] + [2, 3] + [4]

max(range(10))
min(range(10), key=lambda x: (x-2)*(x-4))
all([x < 5 for x in range(5)])
perfect_square = lambda x: x == round(x ** 0.5) ** 2
any([perfect_square(x) for x in range(50, 60)]) # Try ,65)



# Dicts

def dict_demos():
    numerals = {'I': 1, 'V': 5, 'X': 10}
    numerals['X']
    # numerals['X-ray']
    # numerals[10]
    len(numerals)
    list(numerals)
    numerals.values()
    list(numerals.values())
    sum(numerals.values())
    dict([[3, 9], [4, 16]])
    numerals.get('X', 0)
    numerals.get('X-ray', 0)
    {1: 2, 1: 3}
    {[1]: 2}
    {1: [2]}

def index(keys, values, match):
    """Return a dictionary from keys k to a list of values v for which 
    match(k, v) is a true value.
    
    >>> index([7, 9, 11], range(30, 50), lambda k, v: v % k == 0)
    {7: [35, 42, 49], 9: [36, 45], 11: [33, 44]}
    """
    return {k: [v for v in values if match(k, v)] for k in keys}

