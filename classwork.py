l = 'Namespaces are one honking great idea -- let\'do more of those!'

####### HomeWork
#d={}
#for letter in set(l):
 #  d[letter]=l.count(letter)

#print(d)

#for k, v in d.items():
 #   print ('{}={}' .format(k,v))

#zipped = d.items()
#print (zipped)

#def value_getter(x):
    #return d[x]

#keys = sorted (d, key=lambda x: d[x])
#keys = sorted (d, key=value_getter, reverse=True)
#for key in keys:
    #print('{}={}'.format(key, d[key]))

############ DEF

#def printer(x, y):
#def printer(y, x=0):
    #print(x, y)

#printer (1, 'b')
#printer (x=4, y=7)

#def whisper(word):

#  print(word.lower())

#def shout(word):
 #   print (word.upper())

#def say(volume, word='i am talking'):
 #   volume(word)

#say(whisper, word='HEYYYYY!!!')
#time = 1
#method = whisper
#for hour in range(10):
 #   if hour>5:
  #  method = whisper


###########
#L=['one', 'two','three']

#def hey():
 #   print ('Hey')



#def catcher(*args):
 #   for _ in args:
  #      if callable(_):
   #         print ('Gotha')
    #        _()
     #   else:
      #      print (_)

#catcher(1,2,3, hey)

    #print args
    #print kwargs
#catcher (1,4,5,one=1,two='two')
#catcher(*L)

#### recurse

a = [[1,2], (3,4, {6:[10,16]})]

#def unwrap(x):
 #   try:
  #      for item in x:
   #         unwrap(x)
    #    return
    #except:
     #   print x
      #  return x

#unwrap(a)


###############
#i = 5
#def f(arg=i):
 #   print arg

#i = 6
#f()

######

def f(a,b, L={}):
    L[a] = b
    return L

print f('1',1)
print f('2',2)
print f('3',3)