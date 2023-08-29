#fractional knapsack
n=int(input("Enter the number of items"))
p=[int(x) for x in input(f"Enter the profits of {n} items").split()]
w=[int(x) for x in input(f"Enter respective weights of {n} items").split()]
m=int(input("Enter the maximum capacity of bag:"))
for i in range(n):
    max=i
    for j in range(i+1,n):
        if p[j]/w[j]>p[max]/w[max]:
            max=j
    p[i],p[max]=p[max],p[i]
    w[i], w[max] = w[max], w[i]
x=[0]*n
u=m
for i in range(n):
    if w[i]>u:
        break
    x[i]=1
    u=u-w[i]
if i<=n:
    x[i]=round(u/w[i],2)
print("\nprofit\tweight\tquantity")
for i in range(n):
    print(f"{p[i]}\t{w[i]}\t{x[i]}")