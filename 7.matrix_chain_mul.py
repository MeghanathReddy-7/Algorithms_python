#Matrix chain multiplication
def mul(p,i,j):
    if i==j:
        return 0
    minimum_cost=float('inf')
    for k in range(i,j):
        count=(mul(p,i,k)+mul(p,k+1,j)+p[i-1]*p[k]*p[j])
        if count<minimum_cost:
            minimum_cost=count
    return minimum_cost
arr=[40, 20, 30, 10, 30]
n=len(arr)
print(mul(arr,1,n-1))
