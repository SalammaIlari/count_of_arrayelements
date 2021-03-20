# function to count elements within given range 
def countInRange(arr, n, x, y): 
	count = 0; 
	for i in range(n): 
		if (arr[i] >= x and arr[i] <= y): 
			count += 1
	return count 
arr = [1,3,5,6,8,9,0] 
n = len(arr) 

# Answer queries 
i = 1
j = 5
print(countInRange(arr, n, i, j))
i = 6
j = 9
print(countInRange(arr, n, i, j)) 

#output:3
#       3       
