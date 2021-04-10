# Although searching # for an element in a hash table can take as long as searching 
# for an element in a linked list O(n) time in the worst case—in practice, hashing performs extremely
# well. Under reasonable assumptions, the average time to search for an element in
# a hash table is O(1).

# The downside of direct addressing is obvious: if the universe U is large, storing
# a table T of size jUj may be impractical, or even impossible, given the memory
# available on a typical computer. Furthermore, the set K of keys actually stored
# may be so small relative to U that most of the space allocated for T would be
# wasted.
# When the set K of keys stored in a dictionary is much smaller than the universe
# U of all possible keys, a hash table requires much less storage than a directaddress
# table. Specifically, we can reduce the storage requirement to Θ(|K|) while
# we maintain the benefit that searching for an element in the hash table still requires
# only O(1) time. The catch is that this bound is for the average-case time, whereas
# for direct addressing it holds for the worst-case time.
# With direct addressing, an element with key k is stored in slot k. With hashing,
# this element is stored in slot h.k/; that is, we use a hash function h to compute the
# slot from the key k. Here, h maps the universe U of keys into the slots of a hash
# table T[0, ... , m-1]

# h: U → {0,1, ... ,m-1} ;
# where the size m of the hash table is typically much less than jUj. We say that an
# element with key k hashes to slot h.k/; we also say that h.k/ is the hash value of
# key k. F The hash function reduces the range of array indices and hence the size of
# the array. Instead of a size of jUj, the array can have size m.

# The worst-case running time for insertion is O.1/. The insertion procedure is fast
# in part because it assumes that the element x being inserted is not already present in
# the table; if necessary, we can check this assumption (at additional cost) by searching
# for an element whose key is x:key before we insert. For searching, the worstcase
# running time is proportional to the sizegth of the list;


# The worst-case behavior of hashing with chaining is terrible: all n keys hash
# to the same slot, creating a list of sizegth n. The worst-case time for searching is
# thus ‚O(n) plus the time to compute the hash function—no better than if we used
# one linked list for all the elements.
# Clearly, we do not use hash tables for their worst-case performance. 
# (Perfect hashing, does provide good worst-case performance when the set of keys is static, however.)
# The average-case performance of hashing depends on how well the hash function
# h distributes the set of keys to be stored among the m slots, on the average.


# Hashmap vs Hashtable
# 1. HashMap is non synchronized. It is not-thread safe and can’t be shared between many 
# threads without proper synchronization code whereas Hashtable is synchronized. It is thread-safe and 
# can be shared with many threads.
# 2. HashMap allows one null key and multiple null values whereas Hashtable doesn’t allow any null key or
#  value.
# 3. HashMap is generally preferred over HashTable if thread synchronization is not needed

# Why HashTable doesn’t allow null and HashMap does?
# To successfully store and retrieve objects from a HashTable, the objects used as keys
# must implement the hashCode method and the equals method. Since null is not an object,
# it can’t implement these methods. HashMap is an advanced version and improvement on the
# Hashtable. HashMap was created later.
def next_prime(N):
    def is_prime(x):
        i = 2
        while i < x:
            if x % i == 0:
                return False
            else:
                i += 1
        return True
    for n in range(N*2 , N*7):
        if is_prime(n):
            return n
        

class HashTable:
    def __init__(self, m = 18):
        # m is the number of slots
        # p is a prime number large enough (larger than m obvously) to accomodate key values k
        # a and b are random numbers help us to create a universal hash function with average complexity
        import random
        self.a = random.randint(1,9)
        self.b = random.randint(1,9) 
        self.p = next_prime(m)
        self.m = m
        self.storage = [ [None] for i in range(m)]
        self.all_keys = []
        self.all_vals = []

    def _hash_func(self,k):
            return ((self.a*k + self.b) % self.p) % self.m

    def add(self, key, val):
        index = self._hash_func(key)
        if self.storage[index] == [None]:
            self.storage[index] = [(key, val)]
        else:
            check = False
            for i, tup in enumerate(self.storage[index]):
                if tup[0] == key:
                    self.storage[index][i] = (key, val)
                    return
                
            self.storage[index].append((key, val))             
        self.all_keys.append(key)
        self.all_vals.append(val)

    def get(self, key):
        index = self._hash_func(key)
        for tup in self.storage[index]:
            if tup[0] == key:
                return tup[1]
    
    def delete(self, key):
        index = self._hash_func(key)
        if self.storage[index] != [None]:
            for i, tup in enumerate(self.storage[index]):
                if tup[0] == key:
                    self.storage[index].pop(i)
                    return
        else:
            raise ValueError("No such a key") 
        
    def showCase(self):
        return self.storage
         
    @property # to check the uniform distribution of keys
    def stats(self):
        stats = []
        for i in range(len(self.storage)):
            stats.append(len(self.storage[i]))
        return stats



###########################

import random
h = HashTable()
for i in range(200):
    h.add(i,random.randint(0,100))


print(h.stats)
