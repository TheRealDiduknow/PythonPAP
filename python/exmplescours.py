def multipleN(n):
    assert type(n)==int and n>0 , "Le nombre doit être > 0"
    for i in range(n,n*6,n):
        print(i, end=' , ')
    print(i+n,"\n")

multipleN(2)
multipleN(3)
#multipleN(-1)