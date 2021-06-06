def add_arr(arr_1,arr_2):
    '''
    Function to add 2 binary numbers array and return the result
    '''
    arr_3=[0]*(max(len(arr_1),len(arr_2))+1)
    k=len(arr_3)-1
    i=len(arr_1)-1
    j=len(arr_2)-1
    carry=0
    while(i>=0 and j >= 0):
        arr_3[k] = (arr_1[i]+arr_2[j] + carry )%2 
        carry=(arr_1[i]+arr_2[j]+ carry)//2
        k-=1
        j-=1 
        i-=1 
    while(i>=0):
        arr_3[k]=(arr_1[i]+carry)%2
        carry=(arr_1[i]+carry)//2
        i-=1
        k-=1
    while(j>=0):
        arr_3[k]=(arr_2[j]+carry)%2
        carry=(arr_2[j]+carry)//2
        j-=1
        k-=1
    if carry:
        arr_3[k]=carry
        
    return arr_3

if __name__ == '__main__':
    # Test case 1
    arr1=[1,1,1,1,1,0]
    arr2=[1,1,1,1,1,1]
    assert [1,1,1,1,1,0,1] == add_arr(arr1,arr2)
    # Test case 2 
    arr1=[1,0,1]
    arr2=[1,1,1,1]
    assert [1,0,1,0,0] == add_arr(arr1,arr2)
    # Test case 3 
    arr1=[1,0,0,0,1,0]
    arr2=[1,1]
    assert [0,1,0,0,1,0,1] == add_arr(arr1,arr2)
    # Test case 4 
    arr1=[1,1,1,1,1,1]
    arr2=[1,1,1,1,1,1]
    assert [1,1,1,1,1,1,0] == add_arr(arr1,arr2)
    
