# import this
from xdg.Menu import sort

L = " Beautiful is better than ugly.\n\
Explicit is better than implicit.\n\
Simple is better than complex.\n\
Complex is better than complicated.\n\
Flat is better than nested.\n\
Sparse is better than dense.\n\
Readability counts.\n\
Special cases aren't special enough to break the rules.\n\
Although practicality beats purity.\n\
Errors should never pass silently.\n\
Unless explicitly silenced.\n\
In the face of ambiguity, refuse the temptation to guess.\n\
There should be one-- and preferably only one --obvious way to do it.\n\
Although that way may not be obvious at first unless you're Dutch.\n\
Now is better than never.\n\
Although never is often better than *right* now.\n\
If the implementation is hard to explain, it's a bad idea.\n\
If the implementation is easy to explain, it may be a good idea.\n\
Namespaces are one honking great idea -- let's do more of those! "
# print L

# test L = 'bbbwww'

# create new dict
Dict = {}

# find new letter

for letter in L:
    if not Dict.has_key(letter):
        Dict[letter] = 1
    else:
        Dict[letter] += 1

# print Dict


# print this list vertically
s = Dict.keys()
s = list(s)
s.sort()
for i in s:
    print (i, Dict[i])


# sort by the frequency number

s = Dict.keys()
s = list(s)
n = input('Sort by frequency:')
n = int (n)-1
s.sort(key=lambda i: i[n])
for i in s:
    print ('%7s' % (i[0]))
