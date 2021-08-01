import heapq

def heapify(heap):
    return heapq.heapify(heap)

def heap_push(heap,val):
    return heapq.heappush(heap,val)

def heap_pop(heap):
    return heapq.heappop(heap)

def heap_pushpop(heap,val):
    return heapq.heappushpop(heap,val)

def heap_replace(heap,val):
    return heapq.heapreplace(heap,val)

def heap_nlargest(num,heap):
    return heapq.nlargest(num,heap)

def heap_nsmallest(num,heap):
    return heapq.nsmallest(num,heap)

if __name__ == "__main__":
    arr=input("Enter the numbers(separated by space): ")
    li=list(map(int,arr.split()))
    heapify(li)                                    #heapify
    print(li)
    heap_push(li,46)                               #pushes the element to the heap and adjusts the heap
    print(li)
    heap_pop(li)                                   #pops the smallest element
    print(li)
    heap_pushpop(li,2)                             #push & pop simultaneously
    print(li)
    heap_replace(li,33)                            #pop and then push the element
    print(li)
    print(heap_nlargest(3,li))                            #n-largest elements from heap 
    print(heap_nsmallest(3,li))                           #n-smallest elements from heap