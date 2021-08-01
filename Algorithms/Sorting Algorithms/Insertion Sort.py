#consider the first element to be sorted and the rest to be unsorted.
#take the first element in the unsorted part(u1) and compare it with the sorted part(s1) elements.
#if u1<s1 then insert u1 in correct index else leave it as it is.
#take next element in the unsorted part and compare with sorted elements.Repeat until all are sorted.
# time complexity--->O(n^2)

def insertion_sort(arr):
    for index in range(1,len(arr)):
        current_ele=arr[index]
        pos=index
        while current_ele<arr[pos-1] and pos >0:
            arr[pos]=arr[pos-1]
            pos=pos-1
        arr[pos]=current_ele
    return arr

if __name__=="__main__":
    arr=input("Enter the array of numbers (separated by space):")
    list1=list(map(int,arr.split(sep=" ")))
    print("The Sorted array is :",insertion_sort(list1))