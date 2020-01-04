# 1.2 解压可迭代对象赋值给多个变量
# 问题
# 如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。 那么怎样才能从这个可迭代对象中解压出 N 个元素出来？
# 解决方案
# Python 的星号表达式可以用来解决这个问题。比如，你在学习一门课程，在学期末的时候， 你想统计下家庭作业的平均成绩，但是排除掉第一个和最后一个分数。
# 如果只有四个分数，你可能就直接去简单的手动赋值， 但如果有 24 个呢？这时候星号表达式就派上用场了：
def avg(*args):
    return args[0]

def drop_first_last(grades):
    first,*middle,last = grades
    return middle

print(drop_first_last("35498746413616"))
print(type(drop_first_last("35498746413616")))



record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name,email,*phone_number = record
print(name)
print(email)
print(phone_number)
print(type(phone_number))
print("====================================================")
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x,y):
    print('foo',x,y)

def do_bar(s):
    print('bar',s)

for tag,*args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

print("================================")

# 星号解压语法在字符串操作的时候也会很有用，比如字符串的分割。
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(fields)
print(homedir)
print(sh)

# 有时候，你想解压一些元素后丢弃它们，你不能简单就使用 * ， 但是你可以使用一个普通的废弃名称，比如 _ 或者 ign （ignore）。
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)