# Created by Ingrid Avendano on 9/30/13. 


# inserts a list of key-values into a hash list
def insert(h,k,v):
    # the hash of a key and the modulus is used to figure out which 
    # index in a list to put the key-value list
    index = hash(k)%100
    found_pair = False

    # goes through the key-value pairs in the bucket of an index 
    # in the hash list
    for pairs in h[index]:
        # checks whether the index has the key already and replaces
        # it with a new value
        if k == pairs[0]:
            pairs[1] = v 
            found_pair = True

    if not found_pair:
        h[index].append([k,v])

    return h
     

# returns the value of a key in a hash list
def get(h,k):
    index = hash(k)%100

    for pairs in h[index]:
        if k == pairs[0]:
            return pairs[1]

    return 0


def main():
    hash_list = range(100)
    hash_list = [[] for i in hash_list]
    # print hash_list
    keep_going = "y"

    # prompts user for a key-value pair
    while keep_going.lower() == 'y':
        key = raw_input("key: ")
        value = raw_input("value: ")
        keep_going = raw_input("Want to add more? ('y' or 'n') ")

        hash_list = insert(hash_list,key,value)
        print hash_list

    key_to_find_value = raw_input("Find value of: ")
    found_value = get(hash_list,key_to_find_value)
    
    print found_value
    # print hash_list


main()