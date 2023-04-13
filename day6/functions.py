def suma(list, n):
    if (n == 0):
        return 0
    return suma(list, n-1) + list[n-1]
    
def delPar(list, n):
    if (n > 0):
        delPar(list, n -1)
        if (n % 2 == 0):
            list.remove(n)
   
l = [1,2,3,4,6,7]
print(l)
delDato(l, 6)
print(l)