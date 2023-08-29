#N_queens
def place(k,i,x):
    for j in range(1,k):
        if x[j]==i or abs(x[j]-i)==abs(j-k):
            return False
    return True
def Nqueens(k,n,x=None):
    if x is None:
        x=[0]*(n+1)
    for i in range(1,n+1):
        if place(k,i,x):
            x[k]=i
            if k==n:
                print(x[1:n+1])
            else:
                Nqueens(k+1,n,x)
n=int(input("Enter n"))
Nqueens(1,n)
