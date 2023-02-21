def pick(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the paragraph returns True. If there are fewer than K such paragraphs, return the empty string.

    Arguments:
        paragraphs: a list of strings
        select: a function that returns True for paragraphs that can be selected
        k: an integer

    >>> ps = ['hi', 'how are you', 'fine']
    >>> s = lambda p: len(p) <= 4
    >>> pick(ps, s, 0)
    'hi'
    >>> pick(ps, s, 1)
    'fine'
    >>> pick(ps, s, 2)
    ''
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    new_paragraphs = []
    for p in paragraphs:
        if select(p):
            new_paragraphs += [p]
    return new_paragraphs[k]
    # END PROBLEM 1
ps = ["hello", "hi", "cat", "dog"]
s = lambda p:len(p)<=4
print(pick(ps, s, 0))