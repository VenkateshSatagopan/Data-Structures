def insertion_sort(arr):
    '''
    Function to perform insertion sorted
    '''
    for j in range(1,len(arr)):
        key=arr[j]
        
        i = j - 1 
        
        while i >= 0 and arr[i] < key :
            arr[i+1] = arr [i]
            i-=1 
         
        arr[i+1] = key 
        
    return arr 
    
 
arr = [1,2,4,3,5,6,7,-3]
print(insertion_sort(arr))
