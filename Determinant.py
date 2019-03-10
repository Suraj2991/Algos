def matr():
    order_mat = int(input("Enter Order of Matrix"))
    mat = np.zeros((order_mat, order_mat))
    for i in range(order_mat):
        x = list(input("Enter row of numbers"))
        mat[i]  = list(map(int, x))
    return mat  

def minor(a, r, c):
    new_mat = np.delete(np.delete(a,(r), axis = 0), (c), axis = 1)
    return new_mat, np.shape(new_mat)[0]-1

def det(x, ordm): 
    if ordm == 0:
        return x[ordm, ordm]
    else:
        fin = 0
        for i in range(ordm+1):
            fin = fin + np.power(-1,i+1+1)*x[0,i]*det(*minor(x,0,i))
        return fin

def main():
    matrix = matr()
    print("The entered matrix is as shown below:")
    print(matrix)
    row = 0
    column = 1
    detr = det(matrix,np.shape(matrix)[0]-1)
    print('Determinant: ', detr)
    
main()