numbers = [1, 2, 3, 4, 5]

def AFNP(list):
    try:
        return list[6]
    except IndexError:
        return None

def LYBL(list):
    idx = 6
    return list[idx] if idx < len(list) else None

print(AFNP(numbers))
print(LYBL(numbers))

a) 'hello'.upper() #HELLO
b) [1, 2, 3].push(4) #attribute error 
c) {'key': 'value'}.get('key') #'value'
d) (12345).length() #attribute error 