import numpy as np
def get_diag(x, i, j):
    if i >j:
        while j != 0:
            j = j-1
            i = i-1
        return np.diag(x,-i)
    elif i < j:
        while i != 0:
            i = i-1
            j = j-1
        return np.diag(x,j)
    elif i == j:
        i = 0
        j = 0
    return np.diag(x,0)

def good(x,y):
    global board
    b = board
    b[x,y] = False
    
    if np.any(b[x,:]) or  np.any(b[:,y]) or np.any(get_diag(b,x,y)):
        b[x,y] = True
        return False
    else:
        b[x,y] = True
        return True  

def trier(n):
    global board
    for i in range(np.shape(board)[0]):
        
        board[n,i] = True
        if n == 7 and good(n,i) == True:
            return True
        elif n < 7 and good(n,i) == True and trier(n+1) == True:
            return True
        board[n,i] = False
    return False


def drawboard():
    global board
    print(np.where(np.where(board == False,0,board) == 1, 'Q', np.where(board == False,0,board)))

def main(): 
    if trier(0) == True:
        drawboard()

board = np.zeros((8,8), dtype=bool)
main()