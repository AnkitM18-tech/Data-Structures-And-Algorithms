def quick_sort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot=arr[0]
        less=[i for i in arr[1:] if i < pivot]
        greater=[i for i in arr[1:] if i >pivot]

    return quick_sort(less) + [pivot] +quick_sort(greater)



if __name__=="__main__":
    arr=input("Enter the array of numbers (separated by space):")
    list1=list(map(int,arr.split(sep=" ")))
    print("The Sorted array is :",quick_sort(list1))


#The key process in quickSort is partition. 
# Target of partitions is, given an array and an element x of array as pivot, 
# put x at its correct position in sorted array and put all smaller elements 
# (smaller than x) before x, and put all greater elements (greater than x) after x. 
# All this should be done in linear time.

#Time Complexity--->O(nlog(n))       O(n) for partitioning, O(log(n)) for stack size if pivot is middle
#average time complexity--->O(nlog(n))