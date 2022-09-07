from array import array
from random import random

floats = array('f', (random() for i in range(10 * 7)))

print(floats)