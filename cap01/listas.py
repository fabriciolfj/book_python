symbols = 'ABC'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print(codes)

unicodes = [ord(symbol) for symbol in symbols if ord(symbol) > 66]
print(unicodes)