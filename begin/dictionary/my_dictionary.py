# key : value

# methods:
#   clear, copy, get, items, keys, update, values

x = {1: "one", 2: "two"}

x["first"] = "one"
x[("Delorme", "Ryan", 1995)] = (1, 2, 3)

print(list(x.keys())) # ['first', 2, 1, ('Delorme', 'Ryan', 1995)]
print(x[1]) # 'one'