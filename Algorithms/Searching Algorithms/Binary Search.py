def binary_search(list1,item):                            # O(log(n))--->Time complexity
    low=0                                                 #The idea of binary search is to use the information 
                                                          #that the array is sorted and reduce the time complexity to O(Log n).
    high=len(list1)-1                                     # We need to sort the array to reduce time complexity.

    while low <= high:
        mid=round((low+high)/2)
        guess=list1[mid]
        if guess == item:                                  #found the item
            return mid
        if guess > item:                                   #guess is too high
            high=mid-1
        else:
            low=mid+1                                      #guess is too low
    return None                                            #item does not exist




if __name__=="__main__":
    array=input("Enter the list of numbers(separated by commas):")
    list1=sorted(list(map(int,array.split(sep=","))))
    item=int(input("Enter the item you want to find:"))
    print(binary_search(list1,item))