#Hash maps are very efficient DS.
#Look up by key--->O(1)
#Insertion/Deletion----->O(1)
#Collision Handling By Linear Probing


class HashTable():
    def __init__(self):
        self.MAX=100
        self.arr=[None for i in range(self.MAX)]

    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.MAX

    def __setitem__(self,key,val):
        h=self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h]=(key,val)
        else:
            new_h=self.find_slot(key,h)
            self.arr[new_h]=(key,val)
        print(self.arr)

    def __getitem__(self,key):
        h=self.get_hash(key)
        if self.arr[h] is None:
            return
        probe_range= self.get_probe_range(h)
        for probe_index in probe_range:
            element=self.arr[probe_index]
            if element is None:
                return
            if element[0] == key:
                return element[1]

    def __delitem__(self,key):
        h=self.get_hash(key)
        probe_range=self.get_probe_range(h)
        for probe_index in probe_range:
            if self.arr[probe_index] is None:
                return
            if self.arr[probe_index][0]==key:
                self.arr[probe_index]=None
        print(self.arr)


    def get_probe_range(self,index):
        return [*range(index,len(self.arr))]+[*range(0,index)]

    def find_slot(self,key,index):
        probe_range=self.get_probe_range(index)
        for probe_index in probe_range:
            if self.arr[probe_index] is None:
                return probe_index
            if self.arr[probe_index][0]== key:
                return probe_index
        raise Exception("HashMap is Full!")