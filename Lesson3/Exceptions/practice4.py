students = {'John': 25, 'Jane': 22, 'Doe': 30}

def get_age(name):
    try:
        print(students[name])
    except KeyError:
        print('That student doesnt go here anymore')

get_age('John')
get_age('jacob')