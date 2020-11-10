def jiech(n):
    if n==1:
       return 1
    else :
        return n*jiech(n-1)
re = jiech(5)
print(re)
def jie(n):
    num=n
    for i in range(1,n):
        #print(i)
        num=num*(i)
    print(num)
jie(5)

