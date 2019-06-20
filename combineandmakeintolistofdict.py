def combinestrings():
    s=input('servername')
    d=input('dbname')
    u=input('username')
    p=input('password')
    res='server={};dbname={};username={};password={}'.format(s,d,u,p)
    return res

def catalot(cs):
    lot=[tuple(i.split('=')) for i in cs.split(';')]
    return lot

def cstodict(cs):
    Dict=dict(catalot(cs))
    return Dict
cs=combinestrings()
a=cstodict(cs)
print(a)


