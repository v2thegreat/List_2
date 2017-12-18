from sys import getsizeof
from list_2 import list_2
from numpy import arange

x1=list(range(10**2))
x2=list(range(10**2))
x3=list(range(10**2))
x4=list(range(10**2))

y1=[getsizeof(list(range(x))) for x in range(10**3)]
y2=[getsizeof(list_2(range(x), dtype=object).arr)+getsizeof(list_2(range(x))) for x in range(10**3)]
y3=[getsizeof(list_2(range(x), dtype=int).arr)+getsizeof(list_2(range(x))) for x in range(10**3)]
y4=[getsizeof(arange(x)) for x in range(10**3)]

try:
    import matplotlib.pyplot as plt
    raise ModuleNotFoundError
    plt.plot(x1,y1, label='Python lists')
    plt.plot(x2,y2, label='list_2 of Object Type')
    plt.plot(x3,y3, label='list_2 of Integer Type')
    plt.plot(x4,y4, label='numpy array')

    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
    plt.show()

except ModuleNotFoundError:
    import warnings
    warnings.warn(message='\n\n'+open("MatplotlibNotFoundWarning.txt").read()+'\n\n\n')
    print('Size of: ')
    print('Item Count', 'Python lists', 'list_2 Obj Type', 'list_2 int Type', 'numpy array', sep='\t\t')
    for x in range(len(x1)):
        print(x,y1[x],y2[x],y3[x],y4[x], sep='\t\t\t', end='\n')
