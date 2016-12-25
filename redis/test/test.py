import redis

'''
    If key already exists and is a string, this command appends the value at the end of the string. 
    If key does not exist it is created and set as an empty string, so APPEND will be similar to SET in this special case.
'''
def redis_append(redis_connection):
    #append Hello World in 'message' key
    for x in 'Hello World':
        redis_connection.append('message', x)

    print("'message' value: ", redis_connection.get('message'))
    print('db size: ', redis_connection.dbsize())
    print("delete 'message' key")
    redis_connection.delete('message')
    print('db size: ', redis_connection.dbsize())

'''
    LPUSH
        Insert all the specified values at the head of the list stored at key. If key does not exist, it is created as empty list before 
        performing the push operations. When key holds a value that is not a list, an error is returned.
        It is possible to push multiple elements using a single command call just specifying multiple arguments at the end of the command. 
        Elements are inserted one after the other to the head of the list, from the leftmost element to the rightmost element. 
        So for instance the command LPUSH mylist a b c will result into a list containing c as first element, b as second element and a as third element.
    
    LPOP
        Removes and returns the first element of the list stored at key.

    LRANGE
        Returns the specified elements of the list stored at key. The offsets start and stop are zero-based indexes, with 0 being the first element 
        of the list (the head of the list), 1 being the next element and so on. These offsets can also be negative numbers indicating offsets 
        starting at the end of the list. For example, -1 is the last element of the list, -2 the penultimate, and so on.

    LINDEX
        Returns the element at index index in the list stored at key. The index is zero-based, so 0 means the first element, 1 the second element and so on. 
        Negative indices can be used to designate elements starting at the tail of the list. Here, -1 means the last element, -2 means the penultimate and so forth.
        When the value at key is not a list, an error is returned.

    LLEN
        Returns the length of the list stored at key. If key does not exist, it is interpreted as an empty list and 0 is returned. 
        An error is returned when the value stored at key is not a list.
'''
def redis_list(redis_connection):

    #push 10 elements o list.
    for x in range(0, 10):
        redis_connection.lpush('number_list', x)
        
    #print all elements of list.
    print(redis_connection.lrange('number_list', 0, -1))

    #print fifth element of list.
    print('fifh element of list:', redis_connection.lindex('number_list', 5))

    #print list size.
    print('list size: ', redis_connection.llen('number_list'))

    #pop all elements of list.
    for x in range(0, 10):
        print(redis_connection.lpop('number_list'))
    
if __name__ == '__main__':
    redis_connection = redis.StrictRedis(host = '192.168.99.100', port = 6379, db = 0)
    
    #APPEND
    redis_append(redis_connection)

    print()

    #LPUSH, LPOP, LRANGE
    redis_list(redis_connection)