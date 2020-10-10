from datetime import datetime

def readURL():
    urls = open('url_list.csv','r').read()
    urls = str(urls).split('\n')
    return urls

def writeResults(url,i):
    f= open('list/'+str(i)+'-results.csv',"w+")
    f.write(url+'\n')
    for i in results:
        f.write(url+', Checked'+'\n')