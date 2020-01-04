# 问题
# 你想实现一个自定义迭代模式，跟普通的内置函数比如 range() , reversed() 不一样。
# 解决方案
# 如果你想实现一种新的迭代模式，使用一个生成器函数来定义它。 下面是一个生产某个范围内浮点数的生成器：
def frange(start,stop,increment):
    x = start
    while x < stop:
        yield x
        x += increment

for n in frange(0,4,0.5):
    print(n)

print(list(frange(0,1,0.125)))

def countdown(n):
    print('Starting to count from', n)
    while n > 0:
         yield n
         n -= 1
    print('Done!')

c = countdown(3)
print(c)
print(next(c))
print('*'*10)
print(next(c))
print(next(c))
print(next(c))

# 为什么用这个生成器，是因为如果用List的话，会占用更大的空间，比如说取0,1,2,3,4,5,6............1000
# 你可能会这样：
# for n in range(1000):
#     a=n
# 这个时候range(1000)就默认生成一个含有1000个数的list了，所以很占内存。
# 这个时候你可以用刚才的yield组合成生成器进行实现，也可以用xrange(1000)这个生成器实现
# yield组合：
# def foo(num):
#     print('Starting...')
#     while n < 100:
#         num +=1
#         yield num
#
# for n in foo(0):
#     print(n)

