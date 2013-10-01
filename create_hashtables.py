# creating hashtables

# function insert(h,k,v)
    # h = hash list
    # k = key
    # v = value
def insert(h,k,v):
    index = (hash(k))%100
    found_pair = False


    # goes through the key-value pairs in the bucket of an index 
    # in the hash list
    for pairs in h[index]:
        if k == pairs[0]:
            pairs[1] = v 
            found_pair = True

    if not found_pair:
        # h[index][len(h[index])] = [k, v]
        h[index].append([k,v])

    return h
     

# function get(h,k) --> v
def get(h,k):
    pass


def main():
    hash_list = range(100)
    hash_list = [[] for i in hash_list]
    # print hash_list
    keep_going = "yes"
    while keep_going.lower() == "yes":
        key = raw_input("key: ")
        value = raw_input("value: ")
        keep_going = raw_input("Want to add more? yes or no? ")

        hash_list = insert(hash_list,key,value)
    
    print hash_list


main()