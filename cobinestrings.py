def combine():
    servername=input('Enter the server name')
    dbname=input('Enter the db name')
    username=input('Enter the username')
    password=input('Enter the password')
    #result='servername='+servername+';dbname='+dbname+';username='+username+';password='+password
    result='servername=%s;dbname=%s;username=%s;password=%s' %(servername,dbname,username,password)
    return(result)

res=combine()
print('%s' %res)
