
def kata_13_december(lst):
    i=0
    while i < len(lst):
        if lst[i]%2==0:
            lst.pop(i)
        else:
            i+=1
    return lst
lst=[1, 2, 2, 2, 4, 3, 4, 5, 6, 7]
resultado=kata_13_december(lst)
print(f"La lista actualizada es:{lst}")