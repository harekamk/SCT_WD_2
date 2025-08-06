#there are 2 rooms, one for entry and the other one for exit. you have to collect coins from any room. owner wants to have exactly K coins.
#given no of rooms N and no of gold coins in N rooms. you have to find room no from where you will start and where you'll exit. 
#for more than one soln possible you provide a soln with smaller starting room no. room no start from 1 to N.
#HINT-find a continuous sub seq whose sum will be exactly equal to K
#eg:INPUT: N=10, K=15, 5 3 7 14 18 1 18 4 8 3   OUTPUT: 1 3

'''def findRoom(N, K, coins):
    start, end, current_sum=0,0,0
    result_start, result_end=0, float('inf')

    while end<N:
        current_sum+=coins[end]
        while current_sum>K:
            current_sum-=coins[start]
            start+=1
        
        if current_sum==K:
            if end-start<result_end-result_start:
                result_start, result_end=start, end
        end+=1
    if result_end==float('inf'):
        return "No solution found"
    else:
        return result_start+1, result_end+1
    
N=int(input("Enter no of rooms:"))
K=int(input("Enter no of coins:"))
coins=list(map(int, input().split()))
result=findRoom(N, K, coins)
print("Enter room no",result[0],"and exit room",result[1])'''


