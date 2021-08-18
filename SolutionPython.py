def binarySearch (array, l, r, x): 
    if r >= l:
        mid = l + (r - l) // 2 
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binarySearch(array, l, mid-1, x)
        else:
            return binarySearch(array, mid + 1, r, x)
    else:
        return -1
  

array = [ 2, 3, 4, 10, 40 ]
x = 10
result = binarySearch(array, 0, len(array)-1, x)
  
if result != -1:
    print ("Index =" , result)
else:
    print ("Element is not present in Array")
