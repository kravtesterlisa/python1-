# import this

L = ''' Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those! '''
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
