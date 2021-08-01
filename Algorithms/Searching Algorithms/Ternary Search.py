def ternary_search(list1,item):                   #the list must be sorted to implement ternary search
    low=0                                         # O(log3(n))---->Time Complexity
    high=len(list1)-1                             # Divide the array in 3 parts and check for the item.
                                                  #To find maximum or minimum of unimodal function
    while low <= high :                           #Unimodal--possesing a single maximum value
        mid1=low+(high-low)//3                    #Parabolic Function
        mid2=high-(high-low)//3

        if list1[mid1]==item:
            return mid1

        if list1[mid2]==item:
            return mid2

        if item < list1[mid1]:
            high= mid1-1

        elif item > list1[mid2]:
            low=mid2+1

        else:
            low= mid1+1
            high=mid2-1

    return None


if __name__=="__main__":
    array=input("Enter the list of numbers(separated by commas):")
    list1=sorted(list(map(int,array.split(sep=","))))
    item=int(input("Enter the item you want to find:"))
    print(ternary_search(list1,item))