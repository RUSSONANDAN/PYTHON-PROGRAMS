def combinestrings():
    s=input('servername')
    d=input('dbname')
    u=input('username')
    p=input('password')
    res='server={};dbname={};username={};password={}'.format(s,d,u,p)
    return res

def catalot(cs):
    return [tuple(i.split('=')) for i in cs.split(';')]

res=combinestrings()

print(catalot(res))
