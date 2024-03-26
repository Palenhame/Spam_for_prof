from time import time


def test1(item):
    return [i for i in range(item)]


def test2(item):
    return (i ** 2 for i in range(item))


start_time = time()
for i in test2(10000):
    print(i)
end_time = time()
print(end_time - start_time)

# 0.14101028442382812
# 0.13899970054626465

# 0.37799978256225586
# 0.13700222969055176

# 0.09199905395507812
# 0.13399934768676758

# 2.334001302719116
# 0.13300085067749023

# 0.039927005767822266
#