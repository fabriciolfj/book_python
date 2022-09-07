from collections import deque
dp = deque(range(10), maxlen=10)

dp.rotate(3)

print(dp)

dp.extend([20, 30])
print(dp)