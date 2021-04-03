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
# running time is proportional to the length of the list;


# The worst-case behavior of hashing with chaining is terrible: all n keys hash
# to the same slot, creating a list of length n. The worst-case time for searching is
# thus ‚O(n) plus the time to compute the hash function—no better than if we used
# one linked list for all the elements.
# Clearly, we do not use hash tables for their worst-case performance. 
# (Perfect hashing, does provide good worst-case performance when the set of keys is static, however.)
# The average-case performance of hashing depends on how well the hash function
# h distributes the set of keys to be stored among the m slots, on the average.



