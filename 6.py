def mean(*args):
    return args

print(mean(1,3))

def mean(**kwargs):
    return kwargs

print(mean(x=1,y=3))
