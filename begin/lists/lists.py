

x = ["first", "second", "third", "fourth"]

print(x[0]) # 'first'
print(x[2]) # 'third'
print(x[-1]) # 'fourth'
print(x[-2]) # 'third'
print(x[1:-1]) # ['second', 'third']
print(x[0:3]) # ['first', 'second', 'third']
print(x[-2:1]) # ['third']


x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

x[1] = "two"
x[8:9] = []
print(x) # [1, 'two', 3, 4, 5, 6, 7, 8]
x[5:7] = [6.0, 6.5, 7.0]
print(x) # [1, 'two', 3, 4, 5, 6.0, 6.5, 7.0, 8]


x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(len(x)) # 9

x.reverse()
print(x) # [9, 8, 7, 6, 5, 4, 3, 2, 1]
