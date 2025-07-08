""""
C
    input: object
    output: updated buffer

    explicit: 
        define two methods, get and put
        put method should add object to first avaiable spot in buffer
        if the buffer is full, replace the oldest element in the buffer
        get method should remove and return the oldest method
            (method added before others)
    implicit:
        return None for get if the buffer is empty
        initialize the buffer class with a number argument to determine the number of spaces it can hold 
O
D   
    classes

    list? to add and remove elements 

    functions:
        get
            determine if the buffer is empty:
                if so then return None
            determine what the smallest number is in the list
            remove the smallest number and return it
        put 
            add an object to buffer in an empty slot 
            determine if the length of list is equal to buffer size:
                if buffer is full override the smallest number
                
        
    algorithm:
        initialize a class with one insance of a buffer size
        hold a constant Buffer list to hold objects
        


how can we determine what the oldest added object is?

E
"""

class CircularBuffer():

    def __init__(self, length):
        self._buffer_length = length
        self._buffer = list()

    def put(self, digit):
        if len(self._buffer) == self._buffer_length:
            self._buffer.pop(0)
            self._buffer.append(digit)
            return
        self._buffer.append(digit)
    
    def get(self):
        return self._buffer.pop(0) if self._buffer else None

    

buffer = CircularBuffer(3)

print(buffer.get() is None)          # True

buffer.put(1)
buffer.put(2)
print(buffer.get() == 1)             # True

buffer.put(3)
buffer.put(4)
print(buffer.get() == 2)             # True

buffer.put(5)
buffer.put(6)
buffer.put(7)
print(buffer.get() == 5)             # True
print(buffer.get() == 6)             # True
print(buffer.get() == 7)             # True
print(buffer.get() is None)          # True

buffer2 = CircularBuffer(4)

print(buffer2.get() is None)         # True

buffer2.put(1)
buffer2.put(2)
print(buffer2.get() == 1)            # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)            # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)            # True
print(buffer2.get() == 5)            # True
print(buffer2.get() == 6)            # True
print(buffer2.get() == 7)            # True
print(buffer2.get() is None)         # True