import array

numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)

len(memv)

print(memv[0])

memv_pct = memv.cast('B')
print(memv_pct.tolist())
print(memv_pct)
memv_pct[5] = 4
print(numbers)