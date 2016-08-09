####### to_weird

a = 'tyuuiopsd pjgyrfdsa'
def to_weird(a):
    i = 0
    result = ''
    for x in a:
        if i % 2 == 0:
            result += x.upper()
        else:
            result += x.lower()
        i += 1
    return result
print to_weird(a)

