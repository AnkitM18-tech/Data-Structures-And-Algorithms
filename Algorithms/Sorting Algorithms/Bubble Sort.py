def bubble_sort(arr):
    n=len(arr)

    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr

if __name__=="__main__":
    arr=input("Enter the array of numbers (separated by space):")
    list1=list(map(int,arr.split(sep=" ")))
    print("The Sorted array is :",bubble_sort(list1))



# O(n^2)------>Time Complexity worst and average
# take a number and keep on comparing to it's next number until the array is sorted