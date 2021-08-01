#Variation of insertion short
#also called "diminishing increment sort"
#Take the list of numbers.Find out the gap/incrementor.
# Create sublist based on gap and sort them using insertion sort algorithm.
#reduce gap and repeat step 3.Stop when gap is 0.
#Time Complexity---->O(n^2)

def shell_sort(arr):
    gap=len(arr)//2
    while gap>0:
        for index in range(gap,len(arr)):
            current_ele=arr[index]
            pos=index
            while pos>=gap and current_ele<arr[pos-gap]:
                arr[pos]=arr[pos-gap]
                pos=pos-gap
            arr[pos]=current_ele
        gap=gap//2
    return arr

if __name__=="__main__":
    arr=input("Enter the array of numbers (separated by space):")
    list1=list(map(int,arr.split(sep=" ")))
    print("The Sorted array is :",shell_sort(list1))