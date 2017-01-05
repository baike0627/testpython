#print('hello')
#print(123)

#f = abs

#print(f(12))

'''
def f(x):
    return x * x



r = map(f, l)
print(r)
print(list(r))

L = []
for n in l:
    L.append(f(n))
print(L)


l = [1,2,3,4,5,6,7]
print(list(map(str, l)))

from functools import reduce
def add(x,y):
    return x * 10 + y
print(reduce(add, l))

def str2int(s):
    def fn(x,y):
        return x * 10 + y
    def char2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    return reduce(fn, map(char2num, s))
print(str2int('123'))

'''
l = [1,2,3,4,5,6,7]

l_str = ['1','2','3','4','5','','s']

def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, l)))

def not_empty(s):
    return s and s.strip()

print(':::',list(filter(not_empty, l_str)))