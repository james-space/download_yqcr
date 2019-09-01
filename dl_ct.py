import requests,bs4,lxml

res = requests.get('https://manhua.fzdm.com/132/001/', verify=False)
try:
    res.raise_for_status()
except Exception as exc:
    print('there was a problem:%s'%(exc))
    
print(len(res.text))

srcFile=open('srcData.txt','wb')
for chunk in res.iter_content(len(res.text)):
    srcFile.write(chunk)
srcFile.close()

nSoup=bs4.BeautifulSoup(res.text,'lxml')
type(nSoup)

elems = nSoup.select('script')
type(elems)
print(len(elems))

targetList=[]
targetURL=target1=''
count_i=0
for data in elems:
    if(-1 != data.text.find('var mhurl')):
        print(count_i)
        targetList.append(data.text.split(';'))
    count_i = count_i + 1

print(targetList)

for pngs in targetList[0]:
    if(pngs.find('var mhurl')==0):
        target1=pngs

print('target1:'+target1)

targetURL=target1.split('=')[1][1:-1]
print(targetURL)
part1='http://p0.manhuapan.com/'+targetURL
print(part1)

res1 = requests.get(part1)

try:
    res1.raise_for_status()
except Exception as exc:
    print('there was a problem:%s'%(exc))
    
print(len(res1.text))

srcFile1=open('First.png','wb')
for chunk in res1.iter_content(len(res1.text)):
    srcFile1.write(chunk)
srcFile1.close()

    
