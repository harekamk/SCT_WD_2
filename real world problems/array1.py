#shift last element to first and the remaining towards their right
#INPUT- array=[],    no of rotations=,        indices to check=
arr=list(map(int, input("Enter integers:").split()))
k=int(input("Enter no of rotations:"))
indices=list(map(int, input("Enter indices positions:").split()))
n=len(arr)

def rotate_once(arr):
    last_element=arr[-1]
    for i in range(n-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=last_element

for i in range(k):
    rotate_once(arr)

result=[arr[i] for i in indices]
print(result)

