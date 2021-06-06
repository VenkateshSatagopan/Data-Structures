def merge(arr,p,q):
    '''
    Function to perform merge- sort
    '''
    if p<q:  # Base condition for recursion
        m = (p + q )//2
        merge(arr,p,m) # Divide left part of array
        merge(arr,m+1,q) # Divide right part of array
        return merge_array(arr,p,m,q) # Merge left and right part of the array
    
def merge_array(arr,p,m,q):
    '''
    Funtion to perform merging operation
    '''
    n1 = m -p + 1
    n2 = q - m 
    left_array = [0] * n1  # temporary array to store left half of array
    right_array= [0] * n2  # temporary array to store right half of the array
    
    for i in range(n1):
        left_array[i]= arr[p+i]
    for i in range(n2):
        right_array[i]=arr[m+1+i]
    
    i=0 # pointer to traverse left half of array
    j=0 # pointer to traverse right half of array
    k=p
    while (i<n1 and j<n2):
        if left_array[i] <= right_array[j]:
            arr[k] = left_array[i]
            i +=1 
        else:
            arr[k] = right_array[j]
            j +=1
        k+=1
    while i<n1:
        arr[k] = left_array[i]
        k+=1
        i+=1 
    
    while j<n2:
        arr[k] = right_array[j]
        j+=1 
        k+=1
        
    return arr
        

arr =[7,8,6,5,4,3,2,1]
print(merge(arr,p=0,q=len(arr)-1))
