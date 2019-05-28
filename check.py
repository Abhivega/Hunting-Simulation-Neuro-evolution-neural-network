global k
k=0

def hai():
    global k
    k=10


def hai2():
    global k
    k = 20

hai()
hai2()
print(k)
