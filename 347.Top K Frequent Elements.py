
def topKFrequent(a,k):
    d = {}
    for x in a:
       d[x] = d.get(x, 0) + 1
    print(d)
    lst = [(x, d[x]) for x in d]
    print(lst)
    lst.sort(reverse=True, key=lambda t:t[1])
    print(lst)
    print(dict(lst[:k]).keys())
    return dict(lst[:k]).keys()

a= [3,2,2,2,1,1,1,1,4,4]
topKFrequent(a,2)


        





