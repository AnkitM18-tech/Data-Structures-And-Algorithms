#Do digit by digit sort starting from least significant digit to most significant digit
#Uses counting sort as a subroutine to sort
#If elements are in range from 1 to n^2 ,radix sort is used ,when in range from 1 to k,counting sort is used.
#Sort input array using counting sort according to the i th digit.i varies from LSD to MSD.
#Time  Complexity--->O((n+b)*(logb(k)))
#b=base of representing numbers,k=max possible value.

def counting_sort(arr,exp1):
    n=len(arr)
    op=[0]*n
    count=[0]*10                   # 0 to 9
    #Store count of occurances
    for i in range(0,n):
        index=(arr[i]//exp1)
        count[(index)%10]+=1
    #Change count[i],so it contains actual pos of the digit in o/p array
    for i in range(1,10):
        count[i]+=count[i-1]
    i=n-1

    while i>=0:
        index=(arr[i]//exp1)
        op[count[(index)%10]-1]=arr[i]
        count[(index)%10]-=1
        i-=1
    i=0
    #copying op to arr,so arr contains sorted nos
    for i in range(0,len(arr)):
        arr[i]=op[i]
    return arr

def radix_sort(arr):
    #max. no to know the no of digits
    max1=max(arr)
    #instead of passing digit,exp is passed
    #exp=10**i,i=current digit count
    exp=1
    while max1//exp>0:
        counting_sort(arr,exp)
        exp*=10
    return arr

if __name__=="__main__":
    arr=input("Enter the array of numbers (separated by space):")
    list1=list(map(int,arr.split(sep=" ")))
    print("The Sorted array is :",radix_sort(list1))