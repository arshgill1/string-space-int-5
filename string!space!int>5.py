import numpy as np

def str_to_list(str):
    l=list(str)

    for i in str:
        if i not in l:
            l+=i

    for i in l:
        if i.isdigit():
            if int(i)>5:
                l.remove(i)

    for i in l:
        if i==" ":
            l.remove(i)
    #return l
    arr=np.asarray(l)
    return arr

n = input("enter anything: ")
print(str_to_list(n))
