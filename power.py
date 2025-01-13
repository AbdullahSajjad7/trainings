def helper(num, pow, res):
    if pow == 0:
        return 1
    if pow == 1:
        return res
    return helper(num, pow - 1, res * num)

def power_func(num, pow):
    flag = pow >= 0
    pow = abs(pow)
    if flag:
        return helper(num, pow, num)
    return 1 / helper(num, pow, num)

print(power_func(4,0))
print(power_func(4,1))
print(power_func(4,-2))
print(power_func(0,0))
print(power_func(0,2))
print(power_func(-4,2))
print(power_func(-4,-2))

