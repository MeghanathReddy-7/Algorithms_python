#job scheduling in python
def printJobScheduling(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j][2]<arr[j+1][2]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
    l=[]
    print(arr)
    for i in  arr:
         l.append(i[1])
    M=max(l)
    job_arr=[False]*(M)
    profit=0
    for i in arr:
        if job_arr[i[1]-1]==False:
              job_arr[i[1]-1]=i[0]
              profit+=i[2]
        else:
             for j in range(i[1]-2,-1,-1):
                  if job_arr[j]==False:
                     job_arr[j]=i[0]
                     profit+=i[2]
    print(job_arr)
    print(profit)
arr = [['a', 2, 100], ['b', 1, 19], ['c', 2, 27],['d', 1, 25],['e', 3, 15]]
print("Following is maximum profit sequence of jobs")
printJobScheduling(arr)