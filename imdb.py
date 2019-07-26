import requests as req
from bs4 import BeautifulSoup as b
url="https://www.imdb.com/movies-in-theaters/?ref_=nv_tp_inth_1"
r=req.get(url)
soup=b(r.content,'lxml')
div=soup.findAll('div',{'class':['list_item odd','list_item even']})

i=0
for x in div:
    print(div[i].tr.h4.a.text)
    s=div[i].tr.p.findAll('span')
    print(" Genre: ",end="")
    for y in s:
        print(" "+y.text,end="")
    print()
    print(" time: ",div[i].time.text)
    m=div[i].find('span',{'class':['metascore favorable','metascore mixed']})
    if(m):
        print(" metascore: ",m.text)
    else:
        print(" metascore: not rated till now")
    t=div[i].findAll('div',class_='txt-block')
    print(" Director: ",end="")
    dir=t[0].findAll('span')
    li=[]
    for di in dir:
        if(di.a):
            li.append(di.a.text)
    g=",".join(li)
    print(g)
    lis=[]
    print(" Stars: ",end="")
    st=t[1].findAll('a')
    for star in st:
        if(star):
            lis.append(star.text)
    g=",".join(lis)
    print(g)
    print("\n")
    i=i+1
    
