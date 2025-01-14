def double_vals(n):
    return n * 2

l = [1,2,3,4,5]
l = map(double_vals, l)
l = list(l)

print(l)
