#batool dya'a shilleh
#11923748
the_lest = []
n = int(input())
x = list(map(int, input().split()))
def divide (beginning,end,arr):
    povitindex = beginning
    povit = arr[povitindex]
    while beginning < end :
        while beginning< len(arr) and arr[beginning] <= povit:
            beginning +=1
        while arr[end] > povit:
            end-=1
        if beginning < end :
            arr[beginning],arr[end] = arr[end],arr[beginning]
    arr[end],arr[povitindex] = arr[povitindex],arr[end]
    return end
def quick (beginning, end , arr):
    if(beginning< end):
        e = divide(beginning,end,arr)
        quick(beginning,e-1,arr)
        quick(e+1,end,arr)
quick(0,len(x)-1,x)
the_lest="["+",".join(str(i) for i in x)+"]"
print(the_lest)