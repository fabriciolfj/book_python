#board = [['_'] * 3] * 3 #esta fazendo referencia mesma lista
board = [['_'] * 3 for i in range(3)]
board[0][0] = 'x'
print(board)


l = list(range(5))

#l = l + [9]
l *= 9
print(l)