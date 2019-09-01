import requests,bs4,lxml

res = requests.get('https://manhua.fzdm.com/132/001/', verify=False)
try:
    res.raise_for_status()
except Exception as exc:
    print('there was a problem:%s'%(exc))
    
print('read total byte:'+str(len(res.text)))

srcFile=open('srcData.txt','wb')
for chunk in res.iter_content(len(res.text)):
    srcFile.write(chunk)
srcFile.close()

nSoup=bs4.BeautifulSoup(res.text,'lxml')
type(nSoup)

elems = nSoup.select('script')
type(elems)
print("scripts byte:"+str(len(elems)))

targetList=[]
target1=[]
tarURL=[]
targetURL=''
count_i=1
for data in elems:
    if(-1 != data.text.find('var mhurl')):
        #print(count_i)
        targetList.append(data.text.split(';'))
    #count_i = count_i + 1

#print(targetList)

for list_1 in targetList:
    for pngs in list_1:
        if(pngs.find('var mhurl')==0):
            print("contain pngs:"+str(pngs))
            target1.append(pngs)

for i in target1:
    print(i)
    targetURL=i.split('=')[1][1:-1]
    print(targetURL)
    part1='http://p0.manhuapan.com/'+targetURL
    tarURL.append(part1)

print(tarURL)

for pages in tarURL:
    res1 = requests.get(pages)
    try:
        res1.raise_for_status()
    except Exception as exc:
        print('there was a problem:%s'%(exc))

    print('png len:'+str(len(res1.text)))

    srcFile1=open(str(count_i)+'.png','wb')
    for chunk in res1.iter_content(len(res1.text)):
        srcFile1.write(chunk)
    srcFile1.close()
    count_i=count_i+1;

