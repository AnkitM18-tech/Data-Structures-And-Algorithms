"""Build a max heap fro i/p data.At this point,the largest item is stored at the root of the heap.
Replace it with the last item of the heap followed by reducing the size of heap by 1.Finally heapify 
the root tree.Repeat while size of heap >1.Heapify procedure can be applied to a node only 
if its children are heapified.So the heapification must be performed in the bottom up order.

Time Complexity---->heapify-->O(log(n)),create and build heap--->O(n),Overall---->O(nlog(n))"""

def heapify(arr,n,i):    #n=size of heap,i=index,Heapify subtree rooted at i.
    largest=i
    l=2*i+1
    r=2*i+2

    #see if left child of root exists &>root
    if l<n and arr[i]<arr[l]:
        largest=l
    #see if right child of root exists &>root
    if r<n and arr[largest]<arr[r]:
        largest=r
    #change root if needed
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
    #Heapify the root
        heapify(arr,n,largest)
    return arr

def heap_sort(arr):
    n=len(arr)
    #build a max heap
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    #extract elements ,replace root with last and remove it.
    for i in range (n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)
    return arr

if __name__=="__main__":
    arr=input("Enter the array of numbers (separated by space):")
    list1=list(map(int,arr.split(sep=" ")))
    print("The Sorted array is :",heap_sort(list1))