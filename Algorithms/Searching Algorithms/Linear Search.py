def linear_search(list1,item):                            # O(n)------>Time Complexity
    for i in range(len(list1)):
        if list1[i]==item:
            return i
    return None

if __name__=="__main__":
    arr=input("Enter the list of numbers (separated with commas) :")
    list1=list(map(int,arr.split(sep=",")))
    item=int(input("Enter the no you want to search :"))
    print(linear_search(list1,item))