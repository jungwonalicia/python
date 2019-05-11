file4 = open('tv.txt', 'r')

def read10():
    for count in range(0, 10):
        data = file4.read()
        print(data)

read10()
