def find_smallest(arr):
    smallest=arr[0]
    smallest_index=0

    for i in range(1,len(arr)):
        if arr[i]<smallest:
            smallest=arr[i]
            smallest_index=i
    return smallest_index

def selection_sort(arr):
    newArr=[]
    for i in range(len(arr)):
        smallest=find_smallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

if __name__=="__main__":
    arr=input("Enter the array of numbers (separated by space):")
    list1=list(map(int,arr.split(sep=" ")))
    print("The Sorted array is :",selection_sort(list1))


#The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering 
# ascending order) from unsorted part and putting it at the beginning.
#  The algorithm maintains two subarrays in a given array.

#1) The subarray which is already sorted.
#2) Remaining subarray which is unsorted.

#In every iteration of selection sort, the minimum element 
# (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.

#O(n^2)----->Time Complexity